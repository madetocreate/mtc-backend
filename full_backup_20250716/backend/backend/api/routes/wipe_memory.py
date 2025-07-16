from fastapi import APIRouter
from api.memory import wipe_memory

router = APIRouter()

@router.post("/wipe_memory")
async def wipe():
    wipe_memory()
    return "✅ Speicher gelöscht."
