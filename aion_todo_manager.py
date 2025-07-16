import os
import shutil

TODO_PATH = "memory/todo/todo_master.md"
DONE_DIR = "memory/todo_done/"
TMP_DIR = "memory/todo_tmp/"

os.makedirs(TMP_DIR, exist_ok=True)

def split_tasks(todo_file):
    with open(todo_file, "r", encoding="utf-8") as f:
        tasks = [line.strip() for line in f if line.strip()]
    for idx, task in enumerate(tasks):
        taskfile = os.path.join(TMP_DIR, f"task_{idx+1}.md")
        with open(taskfile, "w", encoding="utf-8") as tf:
            tf.write(task)
    shutil.move(todo_file, os.path.join(DONE_DIR, f"done_{os.path.basename(todo_file)}"))

if __name__ == "__main__":
    split_tasks(TODO_PATH)
