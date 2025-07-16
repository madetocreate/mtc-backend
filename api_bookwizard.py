from fastapi import FastAPI
from modules.book_wizard import router as book_wizard_router

app = FastAPI()
app.include_router(book_wizard_router.router)

