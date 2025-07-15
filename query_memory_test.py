import requests
res = requests.post("http://localhost:8001/query_memory", json={"query": "Dummy"})
print(res.json())
