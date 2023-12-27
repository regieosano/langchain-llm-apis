import json
from fastapi import HTTPException, Response, status
from app.routers.route.router import post_router
from ..services.api.vector.main import VectorDBService
from models.schemas import PostVector

vector_db_service = VectorDBService()

@post_router.post("/vector", status_code=status.HTTP_200_OK, response_model= str)
def vectordb_llm_query(post_vector_question: PostVector):
	try:
		result = vector_db_service.get_vector_db_response(post_vector_question)
		json_data = json.loads(result.content)
		return json_data
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
