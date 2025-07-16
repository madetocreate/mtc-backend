from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def video(file: str = Body(..., embed=True)):
    return {"video": "Fake video result"}

