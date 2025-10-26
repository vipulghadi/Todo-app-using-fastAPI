from sqlmodel import Field, SQLModel,Relationship
from datetime import datetime

class TaskModel(SQLModel, table=True):
    title=Field(nullable=False,min_length=3,max_length=5)
    start_date=Field(nullable=False,default=datetime.now)
    end_date=Field(nullable=False,default=datetime.now)
    is_completed=Field(nullable=False,default=False)

    is_deleted=Field(nullable=False,default=False)
    created_at=Field(nullable=False,default=datetime.now)
    updated_at=Field(nullable=False,default=datetime.now)

    sub_tasks=Relationship(back_populates='task')

class SubTaskModel(SQLModel, table=True):
    title=Field(nullable=False,min_length=3,max_length=5)
    start_date=Field(nullable=False,default=datetime.now)
    end_date=Field(nullable=False,default=datetime.now)
    is_completed=Field(nullable=False,default=False)
    created_at=Field(nullable=False,default=datetime.now)
    updated_at=Field(nullable=False,default=datetime.now)
    is_deleted=Field(nullable=False,default=False)

    task_id=Field(default=None,foreign_key='TaskModel.task_id')
    task=Relationship(back_populates='sub_tasks')
