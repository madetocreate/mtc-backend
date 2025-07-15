from creator_engine.modules.memory.memory_bridge import memory_save

def code_research(query):
    code_snippet = f"Code Beispiel für: {query}"
    memory_save("code", code_snippet, {"query": query, "source": "codebot"})
    return code_snippet
