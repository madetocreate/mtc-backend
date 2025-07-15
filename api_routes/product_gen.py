from fastapi import APIRouter, Request
from modules.product_gen.logic import run_module
router = APIRouter()
@router.post("/product_gen")
async def product_gen(request: Request):
 data = await request.json()
 return {"output": run_module(data.get("prompt", ""))}
