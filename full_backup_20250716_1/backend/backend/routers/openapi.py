from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def openapi(data: dict = Body(...)):
    return {"result": "Fake OpenAPI call"}

