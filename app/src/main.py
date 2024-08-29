import os
import typer

from loguru import logger
from baseapp import BaseWebapp
from typing_extensions import Annotated
from pywebio.platform.fastapi import start_server

app = typer.Typer()

def spawn_instance():
    instance = BaseWebapp()

@app.command()
def server(
    server_port: Annotated[int, typer.Option(..., envvar=["SERVER_PORT"])] = 5555
):
    start_server(spawn_instance, port= server_port)


if __name__ == "__main__":
    app()