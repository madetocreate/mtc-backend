import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

with open("memory/entries/1.md", "r", encoding="utf-8") as f:
    content = f.read()

system_prompt = "Lies den folgenden Task-Text aus memory/entries/1.md. Extrahiere daraus 3–10 klare Aufgaben als Aion-kompatible Prompts. Formatiere als Liste mit Beschreibung und Ziel."

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": content}
    ]
)

print("📋 Vorschau: Diese Befehle würde Aion ableiten:\\n")
print(response.choices[0].message.content)
