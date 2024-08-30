import os
import typer

from loguru import logger
from baseapp import BaseWebapp
from dotenv import load_dotenv
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
    env_file_path = os.path.abspath(os.path.join(os.path.abspath(__file__),"..","..","..",".env"))
    load_dotenv(env_file_path)
    app()