def save_task(task, project):
    from pathlib import Path
    target = Path(f"memory/projects/{project}/tasks.md")
    with open(target, "a") as f:
        f.write(task + "\n")
def save_summary(project, text):
    with open(f"memory/projects/{project}/summaries.md", "a") as f:
        f.write(text + "\n\n")
def save_task_with_tags(task, project):
    from .tagger import auto_tag
    tags = auto_tag(task)
    with open(f"memory/projects/{project}/tasks.md", "a") as f:
        f.write(f"{task} {tags}\n")
