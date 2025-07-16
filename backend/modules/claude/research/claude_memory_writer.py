def save_to_memory(topic, content):
    with open("memory_logs/claude/research_summary.md", "a") as f:
        f.write(f"## {topic}\n{content}\n\n")
print("Claude Memory Writer bereit")
