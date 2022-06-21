from pathlib import Path

from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse, FileResponse
from jinja2 import Environment, FileSystemLoader

from lw.logger import logger


lwpath = Path(__file__).resolve().parent

app = FastAPI()


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(lwpath / "media" / "favicon.ico")


@app.get("/nashvilleweatherpenis", response_class=FileResponse)
async def nwp():
    return FileResponse(lwpath / "media" / "nashvilleweatherpenis.jpg")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    env = Environment(loader=FileSystemLoader(lwpath))
    template = env.get_template('home.html')
    return HTMLResponse(template.render())


@app.websocket("/ws/")
async def home_websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.receive_text()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("lw.app:app", host="0.0.0.0", port=7654, log_level="info")
