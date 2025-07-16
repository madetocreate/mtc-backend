from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def auth(user: str = Body(..., embed=True)):
    return {"auth": f"Fake login for {user}"}

