from fastapi import APIRouter, Request
router = APIRouter()

@router.post("/video")
async def generate_video(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "Video")
    return { "video_url": f"https://dummy.videos.io/{prompt.replace(' ', '_')}.mp4" }
