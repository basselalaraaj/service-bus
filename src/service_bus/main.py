import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from service_bus.schema import Query

api = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
api.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
