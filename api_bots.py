from fastapi import APIRouter, Request
from bot_memory import load_memory, save_memory

router = APIRouter()

@router.post("/api/bots/toggle")
async def toggle_bot(req: Request):
    data = await req.json()
    bot = data.get("bot", "")
    memory = load_memory()
    if bot in memory:
        memory[bot]["enabled"] = not memory[bot]["enabled"]
    else:
        memory[bot] = {"enabled": True}
    save_memory(memory)
    return {"bot": bot, "enabled": memory[bot]["enabled"]}
