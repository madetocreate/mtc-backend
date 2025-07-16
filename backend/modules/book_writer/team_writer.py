from modules.book_writer.chunker import chunk_text
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def write_chapter(title, prompt):
    messages = [{"role": "user", "content": f"Schreibe ein Kapitel zu: {title}. {prompt}"}]
    result = client.chat.completions.create(model="gpt-4", messages=messages)
    text = result.choices[0].message.content.strip()
    return chunk_text(text)
