from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/")
async def ws_chat(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Fake WS Chat Ready!")
    await websocket.close()

