from config.config_settings import settings
from config.openai import openai_api_key
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from langchain.pydantic_v1 import BaseModel

from supabase.client import Client, create_client

supabase_url = settings.supabase_url
supabase_key = settings.supabase_api_key
supabase: Client = create_client(supabase_url, supabase_key)

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

vector_store = SupabaseVectorStore(
    embedding=embeddings,
    client=supabase,
    table_name="lincoln_speech",
    query_name="match_lincoln",
)


