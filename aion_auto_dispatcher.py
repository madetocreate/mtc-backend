import os
from openai import OpenAI
from dotenv import load_dotenv
import re

load_dotenv()
client = OpenAI()

PREVIEW_FILE = "aion_preview_result.md"
TODO_TMP_DIR = "memory/todo_tmp"
DONE_DIR = "memory/todo_done"
LOGFILE = "memory/ai_task_log.md"

os.makedirs(TODO_TMP_DIR, exist_ok=True)
os.makedirs(DONE_DIR, exist_ok=True)

# Lies die letzte Vorschau (z. B. Ergebnis von aion_preview_prompts.py)
with open(PREVIEW_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Splitte die Prompts (Markdown-basiert)
tasks = re.findall(r"\d+\.\s+\*\*(.+?)\*\*:(.*?)\n\s+- \*\*Ziel:\*\*\s+(.+?)(?=\n\d+\.|\Z)", content, re.DOTALL)
for idx, (title, desc, ziel) in enumerate(tasks, 1):
    todo_text = f"{title.strip()}:\n{desc.strip()}\nZiel: {ziel.strip()}\n"
    taskfile = os.path.join(TODO_TMP_DIR, f"task_{idx}.md")
    with open(taskfile, "w", encoding="utf-8") as tf:
        tf.write(todo_text)

# Jetzt alle Tasks abarbeiten:
for fname in sorted(os.listdir(TODO_TMP_DIR)):
    if fname.endswith(".md"):
        fpath = os.path.join(TODO_TMP_DIR, fname)
        print(f"\n🚀 Bearbeite Task: {fname}")
        with open(fpath, "r", encoding="utf-8") as tf:
            prompt = tf.read()
        # Sende an GPT zur Bearbeitung
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Bearbeite folgende Aufgabe als eigenständigen Task. Gib einen Lösungsansatz oder Implementierungsschritte."},
                {"role": "user", "content": prompt}
            ]
        )
        print("Antwort:\n", response.choices[0].message.content)
        # Logging (AI-Antwort speichern)
        with open(LOGFILE, "a", encoding="utf-8") as log:
            log.write(f"\n# {fname}\n")
            log.write(prompt)
            log.write("\n## Antwort:\n")
            log.write(response.choices[0].message.content)
            log.write("\n" + "="*40 + "\n")
        os.rename(fpath, os.path.join(DONE_DIR, fname))
