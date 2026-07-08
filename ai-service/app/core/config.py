from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CareerLens AI Service"
    app_version: str = "0.1.0"
    openai_api_key: str | None = None
    chroma_host: str = "localhost"
    chroma_port: int = 8001

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
