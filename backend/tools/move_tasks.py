import shutil
from pathlib import Path
source = Path("memory/todo/creative_tasks.md")
target = Path("memory/projects/buchprojekt_nlp/tasks.md")
shutil.copy(source, target)
