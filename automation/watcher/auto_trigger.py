# Auto-Trigger für Task-Events in memory/entries
import os, time
while True:
  files = os.listdir("memory/entries")
  for f in files:
    if f.endswith(".md"):
      os.system("python3 tools/query_memory_gpt.py "+os.path.join("memory/entries",f))
  time.sleep(10)
