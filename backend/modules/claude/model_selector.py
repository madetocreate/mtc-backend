import os

def choose_claude_model(task_complexity="low"):
    if task_complexity == "low":
        return os.getenv("CLAUDE_HAIKU", "claude-3-haiku")
    elif task_complexity == "medium":
        return os.getenv("CLAUDE_SONNET", "claude-3-sonnet")
    return os.getenv("CLAUDE_OPUS", "claude-3-opus")
