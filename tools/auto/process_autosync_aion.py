def load_text(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def save_text(path, text):
    with open(path, "w") as f:
        f.write(text)

info = load_text("memory/ai_generated/info_latest.md")
raw_tasks = load_text("memory/todo/todo_autosync.md")

tasks = []
for line in raw_tasks.split('\n'):
    clean = line.strip()
    if clean:
        tasks.append(f"Task: {clean}")

if tasks:
    output = "# Automatisch generierte Tasks aus todo_autosync.md\n\n"
    for i, t in enumerate(tasks, 1):
        output += f"{i}. {t}\n"
    save_text("memory/todo/auto_tasks.md", output)

print("AION: Info geladen, Tasks strukturiert:", len(tasks), "Tasks erstellt.")
