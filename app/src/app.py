import os
import uvicorn

from server import Server
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import RedirectResponse
from pywebio.platform.fastapi import webio_routes


app = FastAPI()
webserver = Server()

@app.get("/")
async def redirect_root():
    return RedirectResponse("/page1")

app.mount("/page1", FastAPI(routes=webio_routes(webserver.render_example_page)))
app.mount("/page2", FastAPI(routes=webio_routes(webserver.render_example_page2)))

if __name__ == "__main__":
    uvicorn.run(
        app,
        port=int(os.environ.get("APP_PORT", default=15533))
    )