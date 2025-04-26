from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path
import yaml


class BaseConfig(BaseSettings):
    """Базовый класс для конфигурации"""

    model_config = SettingsConfigDict(
        env_file=(
            Path(__file__).parent.parent / ".env.local",
            Path(__file__).parent.parent / ".env"
        ),
        env_file_encoding="utf-8",
        extra="ignore"
    )


class DBSettings(BaseConfig):
    """Настройки базы данных"""
    POSTGRES_USER: str = Field(..., alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., alias="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., alias="POSTGRES_DB")
    POSTGRES_HOST: str = Field("localhost", alias="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, alias="POSTGRES_PORT")


class BotSettings(BaseConfig):
    """Настройки бота"""
    BOT_TOKEN: str = Field(..., alias="BOT_TOKEN")
    REDIS_HOST: str = Field(default="localhost", alias="REDIS_HOST")
    REDIS_PORT: int = Field(default=6379, alias="REDIS_PORT")


class AIConfig(BaseSettings):
    """Настройки AI из YAML"""
    ai_service: str
    model: str
    api_key: str
    base_url: str


class Settings(DBSettings, BotSettings):
    """Объединенная конфигурация"""

    @classmethod
    def load_ai_config(cls, config_path: Path = None) -> AIConfig:
        """Загрузка AI конфига из YAML"""
        path = config_path or Path(__file__).parent.parent / "ai_config.yaml"
        with open(path) as f:
            config_data = yaml.safe_load(f)
        return AIConfig(**config_data)

    model_config = SettingsConfigDict(
        env_prefix="BOT_",
        case_sensitive=False
    )


settings = Settings()
ai_config = settings.load_ai_config()