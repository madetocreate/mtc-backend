from .router_config import select_model

def execute(prompt):
    model = select_model(prompt)
    print(f"📦 Modell gewählt: {model}")
    return model

