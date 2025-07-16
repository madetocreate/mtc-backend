import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def write_chapter(book_title, chapter_title, style="neutral", context=None):
    prompt = f"Schreibe das Kapitel '{chapter_title}' für das Buch '{book_title}' im Stil '{style}'."
    if context:
        prompt += f" Berücksichtige folgenden Kontext: {context}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()
