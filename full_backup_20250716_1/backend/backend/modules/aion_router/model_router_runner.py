from modules.router.models.router_executor import execute
with open("prompts/models/test_prompts.txt", "r") as f:
    prompts = f.readlines()
for prompt in prompts:
    prompt = prompt.strip()
    model = execute(prompt)
    print(f"🔀 Prompt: {prompt} → Modell: {model}")
