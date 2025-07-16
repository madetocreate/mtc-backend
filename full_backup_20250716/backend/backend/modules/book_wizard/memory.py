import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "__memory__.json")

def read_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def append_to_memory(category, entry):
    memory = read_memory()
    if category not in memory:
        memory[category] = []
    memory[category].append(entry)
    write_memory(memory)
