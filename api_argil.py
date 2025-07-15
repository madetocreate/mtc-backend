from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import requests, os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

@router.post("/api/video/argil")
async def generate_argil_video(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "")
    style = data.get("style", "default")
    api_key = os.getenv("ARGIL_API_KEY")

    response = requests.post(
        "https://api.argil.ai/v1/video",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"prompt": prompt, "style": style}
    )

    if response.status_code == 200:
        return response.json()
    else:
        return JSONResponse(content={"error": response.text}, status_code=response.status_code)
