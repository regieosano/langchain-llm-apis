from pydantic import BaseModel

class PostChat(BaseModel):
	 question: str


class PostChatResponse(BaseModel):
 	 answer: str
		

class PostVector(BaseModel):
	 question: str


class PostJoke(BaseModel):
   subject: str


class PostJokeResponse(BaseModel):
	 joke: str	 


