import json
import os

MEMORY_PATH = os.path.join("data", "bots", "memory.json")

def load_memory():
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=2)

def update_memory(bot_name, key, value):
    data = load_memory()
    if bot_name in data:
        data[bot_name][key] = value
        save_memory(data)
