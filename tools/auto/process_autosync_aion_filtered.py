import re

def load_text(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def save_text(path, text):
    with open(path, "w") as f:
        f.write(text)

def clean_task(text):
    text = re.sub(r'[^\w\s,.!?-]', '', text)
    text = re.sub(r'([,.!?-])\1+', r'\1', text)
    text = text.strip()
    return text

info = load_text("memory/ai_generated/info_latest.md")
raw_tasks = load_text("memory/todo/todo_autosync.md")

tasks = []
for line in raw_tasks.split('\n'):
    clean = line.strip()
    if clean:
        cleaned = clean_task(clean)
        if len(cleaned) > 3:
            tasks.append(f"Task: {cleaned}")

if tasks:
    output = "# Gefilterte und bereinigte Tasks aus todo_autosync.md\n\n"
    for i, t in enumerate(tasks, 1):
        output += f"{i}. {t}\n"
    save_text("memory/todo/auto_tasks_filtered.md", output)

print(f"AION: Info geladen, {len(tasks)} gefilterte Tasks erstellt.")
