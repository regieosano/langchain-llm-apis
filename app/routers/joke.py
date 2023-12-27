import json
from app.routers.route.router import post_router
from fastapi import HTTPException, Response, status
from ..services.api.jokes.main import JokeService
from models.schemas import PostJoke, PostJokeResponse

joke_service = JokeService()

@post_router.post("/joke", status_code=status.HTTP_200_OK, response_model=PostJokeResponse)
def joke_llm_elicit(post_joke_elicit: PostJoke):
	try:
		result = joke_service.get_ai_generated_joke(post_joke_elicit.subject)
		
		json_data = json.loads(result.content)
		return json_data
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))