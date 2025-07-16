def save_to_memory(topic, result):
    with open("modules/claude/research/docs/research_memory_log.md", "a") as f:
        f.write(f"\n## {topic}\n{result}\n")
