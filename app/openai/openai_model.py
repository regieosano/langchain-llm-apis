from config.config_settings import settings
from langchain.chat_models import ChatOpenAI

openai_api_key = settings.openai_api_key

model = ChatOpenAI(openai_api_key=openai_api_key)
