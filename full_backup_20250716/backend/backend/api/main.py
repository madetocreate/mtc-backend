from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api import openai_api

app = FastAPI()

# CORS aktivieren, wenn lokal mit Browser gearbeitet wird
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routen einbinden
app.include_router(openai_api.router)

# Frontend statisch servieren
app.mount("/", StaticFiles(directory="public", html=True), name="static")
