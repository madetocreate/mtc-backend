import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

def write_chapter_claude(title, prompt):
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        temperature=0.7,
        system="Du bist ein professioneller Romanautor. Schreibe mit Tiefe, Spannung und Stil.",
        messages=[{"role":"user","content":f"Schreibe das Kapitel {title}. Thema: {prompt}"}]
    )
    return message.content[0].text.strip()
