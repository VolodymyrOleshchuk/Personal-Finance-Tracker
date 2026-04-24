from pydantic_settings import BaseSettings, SettingsConfigDict


# Application settings loaded from environment variables or .env file
class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./finance_tracker.db"
    SECRET_KEY: str = "supersecretkey123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Read variables from .env and ignore extra values
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Global settings instance used across the app
settings = Settings()