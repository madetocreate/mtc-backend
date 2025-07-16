import os
from datetime import datetime

ENTRIES_PATH = "memory/entries"
INDEX_LOG = "memory/index/index_log.md"

def index_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Filter Placeholder (kommt später)
    return content[:500] + "\n\n...[gekürzt für Index]..."

def append_to_index(file, summary):
    with open(INDEX_LOG, "a", encoding="utf-8") as log:
        log.write(f"\n### {file} - {datetime.now().isoformat()}\n{summary}\n")

if __name__ == "__main__":
    for fname in os.listdir(ENTRIES_PATH):
        if fname.endswith(".md"):
            fpath = os.path.join(ENTRIES_PATH, fname)
            summary = index_file(fpath)
            append_to_index(fname, summary)
