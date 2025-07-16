import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_structure(book_title, style="neutral"):
    prompt = f"Erstelle eine sinnvolle Kapitelgliederung für das Buch '{book_title}' im Stil '{style}'. Liste die Kapitel als Stichpunkte auf."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    text = response.choices[0].text.strip()
    chapters = [line.strip('- ').strip() for line in text.split('\n') if line.strip()]
    return '\\n'.join(chapters)
