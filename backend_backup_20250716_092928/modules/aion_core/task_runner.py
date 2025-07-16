import os
from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
from openai import OpenAI

client = OpenAI()

def run_tasks(file_path):
    print(f"Running tasks from {file_path}")

    if not os.path.exists(file_path):
        print("Task file not found.")
        return

    with open(file_path, "r") as f:
        tasks = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not tasks:
        print("No tasks to run.")
        return

    os.makedirs("memory/results/tasks", exist_ok=True)
    os.makedirs("memory/logs/tasks", exist_ok=True)

    for i, task in enumerate(tasks):
        print(f"→ Running Task {i+1}: {task}")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI developer assistant."},
                {"role": "user", "content": task}
            ]
        )
        output = response.choices[0].message.content.strip()

        result_file = f"memory/results/tasks/task_{i+1:02d}.md"
        with open(result_file, "w") as out:
            out.write(f"# Task {i+1}\n\n**Prompt:** {task}\n\n**Result:**\n{output}\n")

        with open("memory/logs/tasks/task_log.md", "a") as log:
            log.write(f"{datetime.now().isoformat()} | Task {i+1} | {task}\n")

    print(f"✅ {len(tasks)} tasks completed.")
