from modules.claude.claude_client import claude_client
def run_claude_prompt(prompt):
 return claude_client.messages.create(model="claude-3-opus-20240229", max_tokens=1024, messages=[{"role": "user", "content": prompt}])
