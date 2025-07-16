from modules.aion_core.aion_task_delegate import delegate_to_aion
from pathlib import Path
import os

def run_tasks(path):
    with open(path) as f:
        tasks = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    for idx, task in enumerate(tasks):
        print(f"→ Lern-Task {idx+1}: {task}")
        result = delegate_to_aion(task)
        with open("memory_logs/learning/learn_log.md", "a") as log:
            log.write(f"\n✅ Lern-Task {idx+1}: {task}\n{result}\n")

if __name__ == "__main__":
    run_tasks("memory/todo/learning_tasks.md")
