import uvicorn

if __name__ == "__main__":
    uvicorn.run("service_bus.main:app", host="127.0.0.1")
