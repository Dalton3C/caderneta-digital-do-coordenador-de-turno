from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./caderneta.db"
    SECRET_KEY: str = "muda-isto-em-desenvolvimento"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()