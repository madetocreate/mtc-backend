import json, time, os
LOG_PATH = os.path.join(os.path.dirname(__file__), "prompt_log.json")

def log_prompt(module, prompt):
    with open(LOG_PATH, "r") as f:
        data = json.load(f)
    entry = {"module": module, "prompt": prompt, "ts": time.time()}
    data.insert(0, entry)
    with open(LOG_PATH, "w") as f:
        json.dump(data[:50], f, indent=2)  # max 50 Einträge
    return entry
