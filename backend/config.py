import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # OpenRouter
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    openrouter_base_url: str = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    
    # Models
    primary_model: str = os.getenv("PRIMARY_MODEL", "mistralai/mistral-7b-instruct")
    fallback_model: str = os.getenv("FALLBACK_MODEL", "meta-llama/llama-2-7b-chat")
    
    # Server
    backend_port: int = int(os.getenv("BACKEND_PORT", 8000))
    backend_host: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # Frontend
    frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    frontend_url_prod: str = os.getenv("FRONTEND_URL_PROD", "")
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # API
    max_query_length: int = int(os.getenv("MAX_QUERY_LENGTH", 1000))
    min_query_length: int = int(os.getenv("MIN_QUERY_LENGTH", 5))
    request_timeout: int = int(os.getenv("REQUEST_TIMEOUT", 60))
    
    # CORS
    cors_origins: List[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    cors_allow_headers: List[str] = ["*"]
    
    class Config:
        env_file = ".env"

settings = Settings()
