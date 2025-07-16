import os
from pathlib import Path
def ensure_project(project):
    path = Path(f"memory/projects/{project}")
    path.mkdir(parents=True, exist_ok=True)
    (path / "tasks.md").touch(exist_ok=True)
    (path / "README.md").touch(exist_ok=True)
    (path / "summaries.md").touch(exist_ok=True)
