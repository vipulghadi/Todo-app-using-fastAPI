from fastapi import APIRouter
from .service import AuthService
from .schema import UserRegisterSchema
from ..core.api_response import api_response
router = APIRouter()

@router.post("/register")
def register_user(user: UserRegisterSchema):
    service = AuthService()
    service.register_user(first_name=user.first_name,
                          last_name=user.last_name,
                          email=user.email,
                          password=user.password)

    return  api_response(
        status_code=200,
        message="successfully registered",
        success=True,
        data={"message": "successfully registered"}
    )




@router.post("/verify-new-user")
def verify_new_user():
    return {"message": "successfully verified"}

    return True
@router.post("/login")
def login_user():
    return {"message": "successfully logged in"}

@router.get("/current-user")
def current_user():
    return {"message": "Weepul is current User"}
