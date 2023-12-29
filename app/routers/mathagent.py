from fastapi import HTTPException, status
from app.routers.route.router import post_router
from ..services.api.math.main import MathService
from models.schemas import PostMath

math_agent_service = MathService()


@post_router.post("/math-agent", status_code=status.HTTP_200_OK)
def math_agent_query(post_math_question: PostMath):
    try:
        result = math_agent_service.get_ai_agent_answer(post_math_question.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
