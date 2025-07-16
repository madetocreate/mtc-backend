from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_commit():
    return {"status": "commit-ok"}

