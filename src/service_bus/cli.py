import logging
import os
import sys

import click
import uvicorn
from uvicorn import main as uvicorn_main

from service_bus import __version__, config

from .main import *  # noqa
from service_bus.exceptions import DispatchException
from service_bus.logging import configure_logging

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

log = logging.getLogger(__name__)


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@click.group()
@click.version_option(version=__version__)
def service_bus_cli():
    """Command-line interface to Dispatch."""
    configure_logging()


@service_bus_cli.group("server")
def service_bus_server():
    """Container for all dispatch server commands."""
    pass


@service_bus_server.command("develop")
@click.option(
    "--log-level",
    type=click.Choice(["debug", "info", "error", "warning", "critical"]),
    default="debug",
    help="Log level to use.",
)
def run_server(log_level):
    """Runs a simple server for development."""
    # Uvicorn expects lowercase logging levels; the logging package expects upper.
    os.environ["LOG_LEVEL"] = log_level.upper()
    import atexit
    from subprocess import Popen

    p = Popen(["yarn", "watch"],
              cwd="src/service_bus/static/service_bus")
    atexit.register(p.terminate)
    uvicorn.run("service_bus.main:app", debug=True,
                reload=True, log_level=log_level)


@service_bus_server.command("start")
def run_server():
    import atexit
    from subprocess import Popen

    p = Popen(["yarn", "build"],
              cwd="src/service_bus/static/service_bus")
    atexit.register(p.terminate)
    uvicorn.run("service_bus.main:app")


def entrypoint():
    """The entry that the CLI is executed from"""
    try:
        service_bus_cli()
    except DispatchException as e:
        click.secho(f"ERROR: {e}", bold=True, fg="red")


if __name__ == "__main__":
    entrypoint()
