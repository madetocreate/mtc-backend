from fastapi import APIRouter, Request
from modules.research_bot.logic import run_module

router = APIRouter()

@router.post("/research_bot")
async def research_bot(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    return {"output": run_module(prompt)}
