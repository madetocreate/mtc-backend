import os, shutil, datetime, json

def upload_to_memory(filepath):
  filename = os.path.basename(filepath)
  timestamp = datetime.datetime.now().isoformat()
  dest_path = f"memory/entries/{filename}"
  shutil.copy(filepath, dest_path)
  log = { "filename": filename, "timestamp": timestamp, "path": dest_path }
  with open("memory_logs/uploads/upload_metadata.json", "a") as f: f.write(json.dumps(log)+"\n")
  print(f"✅ Datei {filename} wurde ins Memory hochgeladen.")
