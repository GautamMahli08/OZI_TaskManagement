from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    DATABASE_NAME: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # Email Verification Token
    VERIFICATION_TOKEN_SECRET: str
    VERIFICATION_TOKEN_EXPIRE_MINUTES: int = 15

    # Email Configuration
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = False

    # Frontend URL
    FRONTEND_URL: str = "http://localhost:5173"

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:5173"]

    # Application
    APP_NAME: str = "Task Management API"
    DEBUG: bool = True

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "allow"  # This allows extra fields from .env
    }

settings = Settings()