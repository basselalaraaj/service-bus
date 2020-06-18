import uvicorn

if __name__ == "__main__":
    uvicorn.run("service_bus.main:api", host="0.0.0.0")
