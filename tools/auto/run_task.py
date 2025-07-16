import sys
import time
import logging
import subprocess

logging.basicConfig(filename='logs/auto/task_execution.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def build_master_architecture(task_desc):
    logging.info("Master-Architektur wird gebaut...")
    time.sleep(2)

def setup_aion(task_desc):
    logging.info("AION Setup wird durchgeführt...")
    time.sleep(2)

def build_codebot(task_desc):
    logging.info("CodeBot wird gebaut...")
    time.sleep(2)

def make_stub(task_name):
    def stub(task_desc):
        logging.info(f"Stub-Funktion für Task '{task_name}' läuft...")
        time.sleep(1)
    return stub

TASK_FUNCTIONS = {
    'Master-Architektur': build_master_architecture,
    'AION': setup_aion,
    'CodeBot': build_codebot,
}

def git_commit_and_push(task_desc):
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f'Automatischer Commit: Task \"{task_desc}\" abgeschlossen'], check=True)
        subprocess.run(['git', 'push'], check=True)
        logging.info(f'Git-Push erfolgreich für Task: {task_desc}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Git-Push fehlgeschlagen: {e}')

def get_task_function(task_desc):
    for key in TASK_FUNCTIONS:
        if key.lower() in task_desc.lower():
            return TASK_FUNCTIONS[key]
    stub_name = task_desc.strip()
    if stub_name not in TASK_FUNCTIONS:
        TASK_FUNCTIONS[stub_name] = make_stub(stub_name)
    return TASK_FUNCTIONS[stub_name]

def run_task(task_desc):
    print(f"Starte Task: {task_desc}")
    logging.info(f"Starte Task: {task_desc}")
    try:
        func = get_task_function(task_desc)
        func(task_desc)
        git_commit_and_push(task_desc)
        print(f"Task abgeschlossen: {task_desc}")
        logging.info(f"Task abgeschlossen: {task_desc}")
        return True
    except Exception as e:
        print(f"Fehler bei Task '{task_desc}': {e}")
        logging.error(f"Fehler bei Task '{task_desc}': {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte Taskbeschreibung als Parameter übergeben.")
        sys.exit(1)
    task = sys.argv[1]
    run_task(task)
