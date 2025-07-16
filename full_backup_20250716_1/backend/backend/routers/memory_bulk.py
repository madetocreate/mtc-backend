from fastapi import APIRouter, Body
from services.memory_bulk import fake_memory_bulk

router = APIRouter()

@router.post("/")
async def bulk(data: list = Body(...)):
    return await fake_memory_bulk(data)

