from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #App Meta Data
    app_name: str = "Enterprise Agentic AI Copilot"
    app_version: str = "0.2.0"
    environment: str = "development"

    #RAG Config 
    rag_embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    rag_chroma_path: str = "./data/processed/chroma"

    #LLM Generation  Config 
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"

    #Instruct Pydeantic to  read from a .enev file and ignore extra variables
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Cach setting 
@lru_cache
def get_settings() -> Settings:
    return Settings()
