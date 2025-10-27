
from pydantic import BaseModel,Field,field_validator,ValidationError

class UserLoginSchema(BaseModel):
    email: str = Field()
    password: str = Field()

    @field_validator("email")
    @classmethod
    def validate_email(cls, value:str):
        if len(value) < 3:
            raise ValueError("Email must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("Email must be less than 100 characters")
        return value.lower()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str):
        if len(value) < 3:
            raise ValueError("Password must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("Password must be less than 100 characters")
        return value.lower()

class UserRegisterSchema(BaseModel):
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field()
    password: str = Field()

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, value:str):
        if len(value) < 3:
            raise ValueError("First name must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("First name must be less than 100 characters")

        return value.lower()

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, value:str):
        if len(value) < 3:
            raise ValueError("Last name must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("Last name must be less than 100 characters")
        return value.lower()

    @field_validator("email")
    @classmethod
    def validate_email(cls, value:str):
        if len(value) < 3:
            raise ValueError("Email must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("Email must be less than 100 characters")
        return value.lower()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str):
        if len(value) < 3:
            raise ValueError("Password must be at least 3 characters")
        elif len(value) > 100:
            raise ValueError("Password must be less than 100 characters")
        return value.lower()

class CurrentUserSchema(BaseModel):
    email: str = Field()
    first_name: str = Field()
    last_name: str = Field()






