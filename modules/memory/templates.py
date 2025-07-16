from creator_engine.modules.memory.core import append_entry

def save_template(title, text, type="text"):
    meta = {"type": type}
    return append_entry("templates", text, {"title": title, **meta})
