from routers.health import router as health_router
from fastapi import FastAPI
from routers.aion import router as aion_router
from routers.memory import router as memory_router
from routers.tts import router as tts_router
from routers.whisper import router as whisper_router
from routers.health import router as health_router
from routers.github_push import router as github_router

app = FastAPI()
app.include_router(aion_router, prefix="/api/v1/aion")
app.include_router(memory_router, prefix="/api/v1/memory")
app.include_router(tts_router, prefix="/api/v1/tts")
app.include_router(whisper_router, prefix="/api/v1/whisper")
app.include_router(health_router, prefix="/api/v1/health")
app.include_router(github_router, prefix="/api/v1/github")
from routers.root import router as root_router
app.include_router(root_router, prefix="")
app.include_router(health_router, prefix='/api/v1/health')
