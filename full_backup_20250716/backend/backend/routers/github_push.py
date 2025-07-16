from fastapi import APIRouter, Body
from services.github import push_to_github
router = APIRouter()
@router.post("/")
def push(file_path: str = Body(...), content: str = Body(...), message: str = Body(...)):
    push_to_github("madetocreate/mtc-backend", file_path, content, message)
    return {"status": "pushed"}
