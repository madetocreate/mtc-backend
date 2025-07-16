from creator_engine.modules.memory.core import append_entry, get_entries, search_memory

append_entry("test", "Das ist ein Test", {"source": "unit", "tag": "demo"})
print(get_entries("test"))
print(search_memory("test"))

