import openai
import os

def review(file_path):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    with open(file_path) as f:
        code = f.read()
    prompt = f"Analysiere folgenden Python-Code und mache Optimierungsvorschläge (Performance, Stil, Sicherheit, Lesbarkeit):\n\n{code[:3000]}"
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    print("Optimierungsvorschläge für", file_path)
    print(resp.choices[0].message.content)
