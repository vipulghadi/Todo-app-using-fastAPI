from sqlalchemy.testing.pickleable import User
from sqlmodel import Session,select
from .schema import UserRegisterSchema
from ..user.models import UserModel
class AuthRepository:
    def __init__(self,session:Session):
        self.session = session

    def create_user(self,user:UserModel):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

    def get_user_by_id(self,id:int):
        return self.session.exec(select(UserModel).where(UserModel.id == id)).first()

    def get_user_by_email(self,email):
        print("email:",email)
        return self.session.exec(select(UserModel).where(UserModel.email == email)).first()

    def get_user_by_email_and_password(self,email,password):
        return self.session.exec(select(UserModel).where(UserModel.email == email,UserModel.password == password)).first()

