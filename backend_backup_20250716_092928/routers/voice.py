from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def voice(data: str = Body(..., embed=True)):
    return {"result": "Fake voice response"}
