from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/")
def marketplace(item: str = Body(..., embed=True)):
    return {"market_result": f"Added {item} to marketplace"}
