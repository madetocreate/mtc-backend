from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def context(data: str = Body(..., embed=True)):
    return {"context": f"Fake context for {data}"}

