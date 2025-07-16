import random

def load_text(path):
    try:
        with open(path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def save_text(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)

prefixes = [
    "Erstelle eine", "Entwickle eine", "Optimiere die", "Implementiere die",
    "Schreibe die", "Erarbeite eine", "Führe aus:", "Starte mit der",
    "Baue die", "Teste die", "Dokumentiere die"
]

raw_tasks = load_text("memory/todo/auto_tasks_filtered.md")

prompts = []
prompts.append("Bitte bearbeite die folgenden Atomic Bots nacheinander:\n\n")

for line in raw_tasks:
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    if "Task:" in line:
        task_text = line.split("Task:",1)[1].strip()
    else:
        task_text = line

    prefix = random.choice(prefixes)
    prompt_line = f"{prefix} {task_text}.\n"
    prompts.append(prompt_line)

prompts.append("\nVielen Dank! Bitte beachte Prioritäten und beste Qualität.\n")

save_text("memory/todo/auto_tasks_prompts.md", prompts)

print(f"AION: {len(prompts)-2} Prompts für Atomic Bots generiert und gespeichert.")
