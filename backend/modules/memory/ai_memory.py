from .core import search_memory

def answer_from_memory(query):
    results = search_memory(query)
    if not results:
        return "Nichts gefunden."
    return "\n".join([r.get("content", "") for r in results[:5]])
