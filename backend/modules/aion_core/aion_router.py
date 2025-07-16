def route_to_claude(user_prompt):
    if "research" in user_prompt.lower() or "long" in user_prompt.lower():
        return "high"
    elif "summarize" in user_prompt.lower() or "quick" in user_prompt.lower():
        return "low"
    return "medium"
