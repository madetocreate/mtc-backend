import requests

MEMORY_API_URL = "http://localhost:8000/memory"

def memory_save(category, content, metadata=None):
    data = {
        "category": category,
        "content": content,
        "metadata": metadata or {}
    }
    res = requests.post(f"{MEMORY_API_URL}/save", json=data)
    return res.json()

def memory_read(category):
    res = requests.get(f"{MEMORY_API_URL}/read/{category}")
    return res.json()
