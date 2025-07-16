from creator_engine.modules.memory.memory_bridge import memory_search

def inject_memory_context(prompt):
    results = memory_search(prompt)
    context = ""
    if results:
        context += "\n\n--- Kontext aus Memory ---\n"
        for r in results[:3]:
            context += f"- {r.get(\"content\")[:300]}...\n"
    return prompt + context
