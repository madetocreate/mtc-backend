import json
import os
import uuid
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "__memory__.json")

def read_memory():
    if not os.path.exists(MEMORY_FILE):
        write_memory({})
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def append_entry(category, content, metadata=None):
    memory = read_memory()
    if category not in memory:
        memory[category] = []
    entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "content": content,
        "metadata": metadata or {}
    }
    memory[category].append(entry)
    write_memory(memory)
    return entry

def get_entries(category, limit=20):
    memory = read_memory()
    return memory.get(category, [])[-limit:]

def search_memory(keyword, category=None):
    memory = read_memory()
    results = []
    for cat, items in memory.items():
        if category and cat != category:
            continue
        for entry in items:
            if keyword.lower() in json.dumps(entry, ensure_ascii=False).lower():
                results.append(entry)
    return results
