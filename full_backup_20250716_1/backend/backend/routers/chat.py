from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def chat(text: str = Body(..., embed=True)):
    return {"reply": f"Fake reply to: {text}"}
