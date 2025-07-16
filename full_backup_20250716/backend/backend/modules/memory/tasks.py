from creator_engine.modules.memory.core import append_entry

def add_task(name, desc, source="manual", status="pending"):
    content = f"{name}: {desc}"
    meta = {"source": source, "status": status}
    return append_entry("tasks", content, meta)
