import sys
import time

def handle_task(task):
    print(f"Bearbeite Task: {task}")
    time.sleep(1)
    print(f"Task {task} erledigt.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Task als Parameter erforderlich")
        sys.exit(1)
    task = sys.argv[1]
    handle_task(task)
