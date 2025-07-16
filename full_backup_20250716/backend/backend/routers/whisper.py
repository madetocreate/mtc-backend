from fastapi import APIRouter, File, UploadFile
from services.whisper_service import fake_whisper
router = APIRouter()
@router.post("/")
async def whisper(file: UploadFile = File(...)):
    return {"text": await fake_whisper(file)}
