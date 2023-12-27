from fastapi import FastAPI
from .routers import chat
from .services.api.chats.main import ChatService

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Lang Chain APIs!"}

@app.get("/favicon.ico")
def favicon():
    return {"message": "Regie's Favicon!"}


app.include_router(chat.router)

