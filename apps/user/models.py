from sqlmodel import SQLModel,Field
from datetime import datetime
from .enums import  RoleEnum

class UserModel(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    first_name: str = Field(min_length=2,max_length=100,nullable=False)
    last_name: str = Field(min_length=2,max_length=100,nullable=False)
    email: str = Field(min_length=5,max_length=255,unique=True)
    phone_number: str = Field(default="")
    role:RoleEnum=Field(default=RoleEnum.USER)
    password: str = Field(max_length=100,nullable=False,min_length=5)
    is_active: bool = Field(default=False)
    is_blocked: bool = Field(default=False)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)



