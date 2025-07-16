def log_score(task, score):
    with open("memory/logs/scored_tasks.log", "a") as f:
        f.write(f"{task} | Score: {score}\n")
