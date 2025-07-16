from fastapi import APIRouter, Request
from modules.head_core.controller import decide_module
router = APIRouter()

@router.post("/route")
async def route_task(request: Request):
    data = await request.json()
    task = data.get("task", "")
    module = decide_module(task)
    return { "target_module": module, "info": f"Head-AI empfiehlt: {module}" }
