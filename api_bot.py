from fastapi import APIRouter, Request
import requests, os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@router.post("/api/bot/send")
async def send_bot_message(req: Request):
    data = await req.json()
    chat_id = data.get("chat_id")
    message = data.get("message")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)
    return response.json()
