from creator_engine.modules.memory.ai_memory import answer_from_memory

def with_memory_context(prompt):
    memory = answer_from_memory(prompt)
    if memory == "Nichts gefunden.":
        return prompt
    return f"{memory}\n\n---\n{prompt}"
