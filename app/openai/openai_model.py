from config.openai import openai_api_key
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(openai_api_key=openai_api_key)
