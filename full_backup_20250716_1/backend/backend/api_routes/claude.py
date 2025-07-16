from fastapi import APIRouter, Request
import os, httpx

router = APIRouter()

@router.post("/claude")
async def claude_real(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    # Placeholder für echte Claude API
    return {"text": f"[Claude Echo-Dummy] {prompt}"}
