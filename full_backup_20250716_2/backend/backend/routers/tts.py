from fastapi import APIRouter, Body
from services.tts_service import tts
router = APIRouter()
@router.post("/")
async def tts_endpoint(text: str = Body(..., embed=True)):
    return {"audio": await tts(text)}
