from .repository import AuthRepository

class AuthService:
    def __init__(self):
        self._auth_repo=AuthRepository()

    def register_user(self,first_name,last_name,email,password):
        pass

    def login_user(self,email,password):
        pass

    def verify_new_user(self):
        pass

    def generate_token(self):
        pass


