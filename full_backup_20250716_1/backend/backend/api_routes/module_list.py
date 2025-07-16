from fastapi import APIRouter
from head_layer.module_list import list_modules

router = APIRouter()

@router.get("/modules")
async def get_modules():
    return list_modules()
