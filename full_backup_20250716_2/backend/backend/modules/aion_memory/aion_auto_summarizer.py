import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_memory_entry(filepath: str):
    with open(filepath, "r") as f:
        content = f.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Fasse den Text intelligent zusammen und extrahiere Titel, Themen & Tags."},
            {"role": "user", "content": content}
        ]
    )

    summary = response.choices[0].message.content.strip()

    # Pfad für neue Datei
    filename = os.path.basename(filepath).replace(".md", ".summary.md")
    save_path = os.path.join("memory/summaries", filename)

    os.makedirs("memory/summaries", exist_ok=True)
    with open(save_path, "w") as f:
        f.write(summary)

    print(f"✅ Zusammenfassung gespeichert unter: {save_path}")
    return summary
