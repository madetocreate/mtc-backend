from fastapi import APIRouter, Request
from modules.three_d_render.logic import run_module

router = APIRouter()

@router.post("/three_d_render")
async def three_d_render(request: Request):
    data = await request.json()
    return {"output": run_module(data.get("prompt", ""))}
