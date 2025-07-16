from fastapi import APIRouter, Body
from services.aion_service import aion_chat
router = APIRouter()
@router.post("/prompt")
async def aion_prompt(prompt: str = Body(..., embed=True)):
    return {"response": await aion_chat(prompt)}
