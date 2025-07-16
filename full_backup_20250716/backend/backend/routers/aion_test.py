from fastapi import APIRouter, Body
from services.aion_service_mock import aion_chat

router = APIRouter()

@router.post("/prompt")
async def aion_prompt(prompt: str = Body(..., embed=True)):
    response = await aion_chat(prompt)
    return {"response": response}
