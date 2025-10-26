from pydantic import BaseModel,Field
from datetime import date
class TodoCreate(BaseModel):
    desc:str=Field(max_length=255,min_length=3)
    date:date=Field()
    is_completed:bool = Field(default=False)

