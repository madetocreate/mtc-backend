from fastapi import APIRouter
from api.routes import query_memory

router = APIRouter()
router.include_router(query_memory.router)
