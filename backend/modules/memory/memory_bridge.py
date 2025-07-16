import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "__memory__.json")

def read_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def write_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def memory_save(category, content, metadata=None):
    memory = read_memory()
    if category not in memory:
        memory[category] = []
    entry = {
        "content": content,
        "metadata": metadata or {},
        "timestamp": datetime.utcnow().isoformat()
    }
    memory[category].append(entry)
    write_memory(memory)
    return entry
