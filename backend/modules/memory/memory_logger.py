def log_task(task):
    with open("memory/logs/memory_log.md", "a") as f:
        f.write(f"TASK: {task}\n")
