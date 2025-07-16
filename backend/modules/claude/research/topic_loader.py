def load_topics():
    with open("memory/todo/learning_tasks.md") as f:
        return [line.strip() for line in f if line.strip()]
