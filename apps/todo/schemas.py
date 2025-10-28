from pydantic import BaseModel,Field,field_validator
from datetime import date


class TodoCreate(BaseModel):
    title:str=Field()
    date:date=Field()
    is_completed:bool = Field(default=False)

    @field_validator('is_completed')
    @classmethod
    def validate_is_completed(cls, v):
        return v

    @field_validator('date')
    @classmethod
    def validate_date(cls, v):
        if not isinstance(v, date):
            raise ValueError("Invalid date format")
        return v

    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if len(v) <3:
            raise ValueError("title is too short")
        elif len(v) > 255:
            raise ValueError("title is too long")
        return v

class TodoDisplay(BaseModel):
    title:str=Field()
    date:date=Field()
    is_completed:bool = Field(default=False)

class TodoUpdate(BaseModel):
    title:str=Field()
    date:date=Field()
    is_completed:bool = Field(default=False)

    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if len(v) <3:
            raise ValueError("title is too short")
        elif len(v) > 255:
            raise ValueError("title is too long")
        return v

    @field_validator('date')
    @classmethod
    def validate_date(cls, v):
        if not isinstance(v, date):
            raise ValueError("Invalid date format")
        return v





