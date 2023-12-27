from fastapi import FastAPI
from .routers import chat, vector
from .services.api.chats.main import ChatService

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Lang Chain APIs!"}

@app.get("/favicon.ico")
def favicon():
    return {"message": "Regie's Favicon!"}


app.include_router(chat.post_router)
app.include_router(vector.post_router)

