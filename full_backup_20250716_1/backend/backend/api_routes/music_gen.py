from fastapi import APIRouter, Request
from modules.music_gen.logic import run_module

router = APIRouter()

@router.post("/music_gen")
async def music_gen(request: Request):
    data = await request.json()
    return {"output": run_module(data.get("prompt", ""))}
