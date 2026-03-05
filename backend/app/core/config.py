from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic import field_validator
import json

class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    SECRET_KEY: str
    DATABASE_URL: str
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return json.loads(v) if isinstance(v, str) else v
        return v

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
