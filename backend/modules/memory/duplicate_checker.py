from pathlib import Path
def is_duplicate(task, project):
    file = Path(f"memory/projects/{project}/tasks.md")
    if not file.exists(): return False
    return task in file.read_text()
