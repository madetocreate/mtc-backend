import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def summarize_memory_entry(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Fasse diesen Text kurz und prägnant zusammen."},
            {"role": "user", "content": content}
        ]
    )
    summary = response.choices[0].message.content
    return summary

def save_summary(original_path, summary):
    filename = os.path.basename(original_path)
    name, _ = os.path.splitext(filename)
    summary_path = f"memory/summaries/{name}_summary.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"✅ Summary gespeichert: {summary_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python3 aion_upload_memory.py memory/entries/DATEI.md")
        sys.exit(1)
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"❌ Datei nicht gefunden: {filepath}")
        sys.exit(1)
    summary = summarize_memory_entry(filepath)
    save_summary(filepath, summary)
