from creator_engine.modules.memory.core import append_entry

def memory_save(category, content, metadata=None):
    return append_entry(category, content, metadata)
