from api.memory import query_memory

results = query_memory("Was war mein erster Gedanke?")
print("\n📚 MEMORY RESULTS:")
for r in results:
    print("🧠", r)
