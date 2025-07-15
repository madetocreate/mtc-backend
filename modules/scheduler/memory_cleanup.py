import time
import threading
from creator_engine.modules.memory.core import read_memory, write_memory

def cleanup_old_entries(max_age_days=30):
    memory = read_memory()
    now = time.time()
    max_age_seconds = max_age_days * 86400
    for category, entries in memory.items():
        memory[category] = [e for e in entries if (now - time.mktime(time.strptime(e["timestamp"], "%Y-%m-%dT%H:%M:%S.%f"))) < max_age_seconds]
    write_memory(memory)
    print("Memory Cleanup durchgeführt.")

def schedule_cleanup(interval_seconds=86400):
    def job():
        while True:
            cleanup_old_entries()
            time.sleep(interval_seconds)
    thread = threading.Thread(target=job, daemon=True)
    thread.start()
