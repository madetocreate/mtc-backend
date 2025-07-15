from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Direktzugriff auf alle Dateien im /public Ordner
app.mount("/", StaticFiles(directory="public", html=True), name="static")
