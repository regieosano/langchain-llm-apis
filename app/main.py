from fastapi import FastAPI
from .routers import chat
from .services.api.chats.main import ChatService

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPIs!"}

app.include_router(chat.router)

