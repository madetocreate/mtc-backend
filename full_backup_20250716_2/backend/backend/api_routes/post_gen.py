from fastapi import APIRouter, Request
from modules.post_gen.logic import run_module
router = APIRouter()
@router.post("/post_gen")
async def post_gen(request: Request):
 data = await request.json()
 return {"output": run_module(data.get("prompt", ""))}
