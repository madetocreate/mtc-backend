import os
import subprocess

entries_dir = "memory/entries"
for file in os.listdir(entries_dir):
    if file.endswith(".md"):
        filepath = os.path.join(entries_dir, file)
        subprocess.run(["python3", "aion_upload_memory.py", filepath])
