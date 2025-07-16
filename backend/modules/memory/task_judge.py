from modules.memory.keyword_filter import is_relevant
from modules.memory.duplicate_checker import is_duplicate
from modules.memory.memory_router import detect_project
from modules.memory.memory_writer import save_task
from modules.memory.memory_logger import log_task

def handle_task(task):
    if not is_relevant(task): return "IGNORED: irrelevant"
    project = detect_project(task)
    ensure_project(project)
    if is_duplicate(task, project): return "IGNORED: duplicate"
    save_task_with_tags(task, project)
    log_task(task)
    update_readme(project, task)
    return f"SAVED to {project}"
from modules.memory.project_tracker import update_readme
from modules.memory.memory_writer import save_task_with_tags
from modules.memory.project_init import ensure_project
