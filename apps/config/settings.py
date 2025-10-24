from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Todo App"
    database_url: str = "sqlite:///./todo.db"
    debug: bool = True

    class Config:
        env_file = ".env"
