from starlette.config import Config
import os
import logging
from distutils.sysconfig import get_python_lib

config = Config(".env")

CONNECTION_STR = config("CONNECTION_STR")

DEFAULT_STATIC_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "static/service_bus/dist"
)

STATIC_DIR = config("STATIC_DIR", default=DEFAULT_STATIC_DIR)

LOG_LEVEL = config("LOG_LEVEL", default=logging.WARNING)
