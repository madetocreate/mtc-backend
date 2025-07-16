from fastapi import APIRouter, Body
from services.memory_service import save_memory
router = APIRouter()
@router.post("/")
async def save(prompt: str = Body(..., embed=True)):
    return {"result": await save_memory(prompt)}
@router.get("/")
def get_memory():
    return {"status": "ok"}
