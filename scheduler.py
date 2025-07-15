import schedule
import time
from ai_task import run_ai_task

def job():
    print("Scheduler startet AI Task...")
    run_ai_task()

schedule.every(10).seconds.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
