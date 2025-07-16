import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

TODO_PATH = "memory/todo/todo_list.md"
DONE_PATH = "memory/todo/done_list.md"

def read_todos():
    if not os.path.exists(TODO_PATH):
        return []
    with open(TODO_PATH, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def write_done(task):
    with open(DONE_PATH, "a", encoding="utf-8") as f:
        f.write(f"✅ {task}\n")

def remove_task(task):
    tasks = read_todos()
    tasks = [t for t in tasks if t != task]
    with open(TODO_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks) + "\n")

def process_task(task):
    print(f"🚀 Bearbeite Aufgabe: {task}")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Erfülle die folgende To-Do-Aufgabe Schritt für Schritt:"},
            {"role": "user", "content": task}
        ]
    )
    result = response.choices[0].message.content
    print(f"✅ Ergebnis:\n{result}")
    write_done(task)
    remove_task(task)

if __name__ == "__main__":
    todos = read_todos()
    for task in todos:
        process_task(task)
