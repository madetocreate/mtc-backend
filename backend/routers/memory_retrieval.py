from fastapi import APIRouter, Body
from services.memory_retrieval import fake_memory_retrieval

router = APIRouter()

@router.get("/{key}")
async def retrieve(key: str):
    return await fake_memory_retrieval(key)

