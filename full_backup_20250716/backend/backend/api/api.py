from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.routes import router as api_router

app = FastAPI()
app.include_router(api_router)
app.mount("/", StaticFiles(directory="public", html=True), name="static")
from api.routes import query_memory
from api.routes import wipe_memory
