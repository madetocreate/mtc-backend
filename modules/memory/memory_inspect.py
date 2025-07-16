import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "__memory__.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def list_categories():
    memory = load_memory()
    return list(memory.keys())

def filter_by_category(category):
    memory = load_memory()
    return memory.get(category, [])

def search_by_keyword(keyword):
    memory = load_memory()
    results = []
    for cat, items in memory.items():
        for entry in items:
            if keyword.lower() in json.dumps(entry).lower():
                results.append({"category": cat, **entry})
    return results

def recent_entries(limit=10):
    memory = load_memory()
    all_entries = []
    for cat, items in memory.items():
        for e in items:
            e["category"] = cat
            all_entries.append(e)
    return sorted(all_entries, key=lambda x: x.get("timestamp", ""), reverse=True)[:limit]

if __name__ == "__main__":
    print("\nLetzte 5 Memory-Einträge:")
    for entry in recent_entries(5):
        print(f"[{entry['category']}] {entry['timestamp']} → {entry['content'][:100]}...")
