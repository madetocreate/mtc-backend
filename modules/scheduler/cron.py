import time
import threading
from creator_engine.modules.book_wizard.autogen.autoflow_trigger import run_autoflow_for_buchideen

def schedule_autoflow(interval_seconds=3600):
    def job():
        while True:
            print("Scheduler: Starte AutoFlow...")
            run_autoflow_for_buchideen()
            time.sleep(interval_seconds)

    thread = threading.Thread(target=job, daemon=True)
    thread.start()
