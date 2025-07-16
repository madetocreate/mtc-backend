def log_to_memory(prompt, output):
    with open("memory/claude_logs/claude_memory_log.md", "a") as log:
        log.write(f"\n\n## PROMPT\n{prompt}\n\n## OUTPUT\n{output}")
