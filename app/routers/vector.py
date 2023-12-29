from fastapi import HTTPException, status
from app.routers.route.router import post_router
from config.vector.main import vector_store
from models.schemas import PostVector, PostVectorStore


@post_router.post("/vector", status_code=status.HTTP_200_OK, response_model=str)
def vectordb_llm_query(post_vector: PostVector):
    try:
        results = vector_store.similarity_search(post_vector.question)

        return results[0].page_content

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@post_router.post("/vector/store", status_code=status.HTTP_200_OK)
def vectordb_llm_store(post_vector_store: PostVectorStore):
    try:
        return post_vector_store
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
