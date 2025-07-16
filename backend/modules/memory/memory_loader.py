import os
from pathlib import Path

def load_tasks(file):
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
