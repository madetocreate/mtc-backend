def decide_module(prompt):
    prompt_lower = prompt.lower()
    if "bild" in prompt or "image" in prompt:
        return "image"
    elif "video" in prompt:
        return "video"
    elif "forschung" in prompt or "recherche" in prompt:
        return "research"
    else:
        return "text"

def run_module(module, prompt):
    return f"Dummy output from {module} module for: {prompt}"
