from fastapi import APIRouter, Request
from api.memory import query_memory

router = APIRouter()

@router.post("/query_memory")
async def memory_query(request: Request):
    data = await request.json()
    query = data.get("query", "")
    results = query_memory(query)
    return {"results": results}
