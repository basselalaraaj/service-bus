import graphene
from starlette.graphql import GraphQLApp
from starlette.applications import Starlette
from starlette.responses import FileResponse, Response, StreamingResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route
import httpx
from os import path

from service_bus.schema import Query
from service_bus.config import STATIC_DIR

# we create the ASGI for the app
app = Starlette(
    routes=[Route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))])

# we create the ASGI for the frontend
frontend = Starlette(
    routes=[Mount("/", StaticFiles(directory=STATIC_DIR), name="app")])


@frontend.middleware("http")
async def default_page(request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        if STATIC_DIR:
            return FileResponse(path.join(STATIC_DIR, "index.html"))
        else:
            async with httpx.AsyncClient() as client:
                remote_resp = await client.get(
                    str(request.url.replace(port=8080)), headers=dict(request.headers)
                )
                return StreamingResponse(
                    remote_resp.aiter_bytes(),
                    headers=remote_resp.headers,
                    status_code=remote_resp.status_code,
                    media_type=remote_resp.headers.get("content-type"),
                )
    return response

app.mount("/", app=frontend)
