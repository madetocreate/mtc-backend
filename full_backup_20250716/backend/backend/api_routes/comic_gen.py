from fastapi import APIRouter, Request
from modules.comic_gen.logic import run_module
router = APIRouter()
@router.post("/comic_gen")
async def comic_gen(request: Request):
 data = await request.json()
 return {"output": run_module(data.get("prompt", ""))}
