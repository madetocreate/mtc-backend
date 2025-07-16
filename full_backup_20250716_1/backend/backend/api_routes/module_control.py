from fastapi import APIRouter, Request
from head_layer.module_manager import toggle_module

router = APIRouter()

@router.post("/toggle_module")
async def toggle_module_route(request: Request):
    data = await request.json()
    module_name = data.get("module")
    result = toggle_module(module_name)
    return result
