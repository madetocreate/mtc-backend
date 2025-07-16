import os

def get_model_by_complexity(level):
    if level == "high": return os.getenv("CLAUDE_1")
    if level == "medium": return os.getenv("CLAUDE_2")
    return os.getenv("CLAUDE_3")
