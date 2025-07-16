from fastapi import APIRouter, Request
from anthropic import Anthropic
import os

router = APIRouter()
claude = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

@router.post("/api/claude")
async def claude_writer(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "")
    response = claude.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response.content[0].text}
