from api.memory import query_memory

frage = input("🔍 Was möchtest du im Memory suchen?\n> ")
resultate = query_memory(frage)

print("\n🧠 Memory-Ergebnisse:")
for eintrag in resultate:
    print("→", eintrag)
