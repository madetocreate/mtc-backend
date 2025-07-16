from fastapi import APIRouter, Request
from modules.head_ai.logic import decide_module, run_module

router = APIRouter()

@router.post("/head_ai")
async def head_ai_controller(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    module = decide_module(prompt)
    result = run_module(module, prompt)
    return {"module": module, "result": result}
