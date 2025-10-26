from sqlmodel import SQLModel, create_engine, Session
from .settings import  get_settings


settings = get_settings()
engine=create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG
)


def get_session():
    with Session(engine) as session:
        yield session

def create_db_tables():
    SQLModel.metadata.create_all(engine)


