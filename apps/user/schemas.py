from pydantic import BaseModel,Field

class UserSchema(BaseModel):
    first_name: str = Field(max_length=100,min_length=3)
    last_name: str = Field(max_length=100,min_length=3)
    email: str = Field(max_length=100,min_length=3)
    phone_number: str = Field(max_length=100,min_length=3)
    password: str = Field(max_length=100,min_length=3)








