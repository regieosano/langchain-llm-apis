from pydantic import BaseModel

class PostChat(BaseModel):
	 question: str


class PostChatResponse(BaseModel):
 	 answer: str
		

class PostVector(BaseModel):
	 question: str



