from starlette.config import Config

config = Config(".env")

CONNECTION_STR = config("CONNECTION_STR")
