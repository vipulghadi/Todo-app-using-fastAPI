from .repository import AuthRepository
from ..user.models import UserModel
from ..core.validators import password_hasher
from ..user.enums import RoleEnum
from .jwt_handler import generate_jwt_token,verify_jwt_token

class AuthService:
    def __init__(self,session):
        self.auth_repo=AuthRepository(session)

    def register_user(self,first_name,last_name,email,password):

        existing_user = self.auth_repo.get_user_by_email(email)
        print(existing_user)
        if existing_user:
            raise ValueError("User exists with given email")

        hashed_password = password_hasher(password)
        self.auth_repo.create_user(UserModel(first_name=first_name,last_name=last_name,email=email,password=hashed_password,role=RoleEnum.USER))


    def login_user(self,email,password):
        existing_user = self.auth_repo.get_user_by_email(email)
        if not existing_user:
            raise ValueError("User does not exist")

        user=self.auth_repo.get_user_by_email_and_password(email,password)
        if not user:
            raise ValueError("User does not exist")


        jwt_token = generate_jwt_token({
            "email": user.email,
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
        return jwt_token







    def verify_new_user(self):
        pass

    def generate_token(self):
        pass


