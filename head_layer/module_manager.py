import json, os

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "module_registry.json")

def load_registry():
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)

def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

def toggle_module(module_name):
    registry = load_registry()
    if module_name in registry:
        registry[module_name]["active"] = not registry[module_name]["active"]
        save_registry(registry)
        return {"module": module_name, "new_state": registry[module_name]["active"]}
    return {"error": "Module not found"}
