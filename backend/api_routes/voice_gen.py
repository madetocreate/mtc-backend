from fastapi import APIRouter, Request
from modules.voice_gen.logic import run_module

router = APIRouter()

@router.post("/voice_gen")
async def voice_gen(request: Request):
    data = await request.json()
    return {"output": run_module(data.get("prompt", ""))}
