import json
from fastapi import HTTPException, Response, status, APIRouter
from ..services.api.chats.main import ChatService
from models.schemas import PostChat, PostChatResponse

router = APIRouter(
	prefix="/api/chat",
	tags=["Posts"]
)

chat_service = ChatService()


@router.post("/", status_code=status.HTTP_200_OK, response_model=PostChatResponse)
def chat_llm_query(post_chat_question: PostChat):
	result = chat_service.get_ai_generated_answer(post_chat_question)
	json_data = json.loads(result.content)
	return json_data
