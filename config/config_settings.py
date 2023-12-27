from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str= ""
    supabase_api_key: str= ""
    openai_api_key: str= ""

    class Config:
        env_file = ".env"


settings = Settings()