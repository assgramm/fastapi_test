import pathlib

from pydantic import BaseSettings

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


class DB(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: str


class SettingsExtractor(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    class Config:
        env_file = BASE_DIR / ".env"


class Settings(BaseSettings):
    db: DB


def load_config() -> Settings:
    settings = SettingsExtractor()

    return Settings(
        db=DB(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            name=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
        )
    )
