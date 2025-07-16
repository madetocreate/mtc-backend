def select_model(prompt):
    if len(prompt) < 80:
        return "gpt-3.5-turbo"
    return "gpt-4"

