#!/bin/bash
cd ~/creator_engine
python3 aion_todo_manager.py
for file in memory/todo_tmp/*.md; do
    python3 aion_upload_memory.py "$file"
    rm "$file"
done
