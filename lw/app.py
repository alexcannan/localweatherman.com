from pathlib import Path

from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse, FileResponse

from lw.logger import logger


lwpath = Path(__file__).resolve().parent

app = FastAPI()


@app.get('/favicon.ico')
async def favicon():
    return FileResponse(lwpath / "favicon.ico")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info(f"we home")
    logger.warning("far out man")
    return HTMLResponse("hello world!")


@app.websocket("/ws/")
async def home_websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.receive_text()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("lw.app:app", host="0.0.0.0", port=7654, log_level="info")
