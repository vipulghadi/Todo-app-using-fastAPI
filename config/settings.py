from pydantic_settings import BaseSettings
import os
from functools import lru_cache
from dotenv import load_dotenv

APP_ENV = os.getenv("APP_ENV","local")
ENV_FILE_MAP = {
    "local": ".env.local",
    "dev": ".env.dev",
    "prod": ".env.prod",
}

env_file = ENV_FILE_MAP.get(APP_ENV,".env.local")
load_dotenv(dotenv_path=env_file)



class Settings(BaseSettings):
    APP_ENV: str = APP_ENV
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = env_file
        env_file_encoding = "utf-8"



@lru_cache()
def get_settings():
    return Settings()