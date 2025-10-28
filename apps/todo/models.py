from sqlmodel import SQLModel,Field
from datetime import datetime,date

class TodoModel(SQLModel, table=True):
    title: str = Field(min_length=3, max_length=255)
    is_completed: bool = Field(default=False)
    date: date = Field(default=date.today)
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)


