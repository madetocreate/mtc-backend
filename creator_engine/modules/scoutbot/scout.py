import queue
from threading import Thread
from creator_engine.modules.memory.memory_bridge import memory_save

task_queue = queue.Queue()

def process_task():
    while True:
        task = task_queue.get()
        if task is None:
            break
        query, domain = task
        # Dummy Recherche-Ergebnis
        result = f"Recherche-Ergebnis für '{query}' in '{domain}'"
        memory_save(domain, result, {"query": query, "source": "scoutbot"})
        task_queue.task_done()

worker_thread = Thread(target=process_task, daemon=True)
worker_thread.start()

def scout_recherche(query, domain="all"):
    task_queue.put((query, domain))
    return f"Recherche-Auftrag für '{query}' in '{domain}' gestartet."

def shutdown_recherche():
    task_queue.put(None)
    worker_thread.join()
