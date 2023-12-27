import json
from fastapi import HTTPException, Response, status
from app.routers.route.router import post_router
from ..services.api.chats.main import ChatService
from models.schemas import PostChat, PostChatResponse 

chat_service = ChatService()

@post_router.post("/chat", status_code=status.HTTP_200_OK, response_model=PostChatResponse)
def chat_llm_query(post_chat_question: PostChat):
	try:
		result = chat_service.get_ai_generated_answer(post_chat_question)
		json_data = json.loads(result.content)
		return json_data
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))


