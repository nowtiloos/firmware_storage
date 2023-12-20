from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # MODE: Literal["DEV", "TEST", "PROD"]
    # LOG_LEVEL: Literal["DEBUG", "INFO"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:"
            f"{self.DB_PASS}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )

    JWT_KEY: str
    JWT_ALGORITHM: str

    FIRMWARE_FOLDER: str
    # SMTP_HOST: str
    # SMTP_PORT: int
    # SMTP_USER: str
    # SMTP_PASS: str
    #
    # REDIS_HOST: str
    # REDIS_PORT: int
    #
    # SENTRY_DSN: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
