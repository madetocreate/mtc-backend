def memory_save(a, b=None, c=None): open("test_memory.txt", "a").write(f"{a},{b},{c}\n")
def read_memory(): return {"test": [{"content": "Testinhalt"}]}
