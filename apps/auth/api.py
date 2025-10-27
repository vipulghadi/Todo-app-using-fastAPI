from fastapi import APIRouter,Depends
from sqlmodel import Session
from .service import AuthService
from .schema import UserRegisterSchema, UserLoginSchema
from ..core.api_response import api_response
from config.database import get_session

router = APIRouter()

@router.post("/register")
def register_user(user: UserRegisterSchema,session: Session = Depends(get_session)):
    service = AuthService(session=session)
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
def login_user(user: UserLoginSchema,session: Session = Depends(get_session)):
    service = AuthService(session=session)
    token=service.login_user(email=user.email,password=user.password)

    return {
        "message": "successfully logged in",
        "success": True,
        "data":{
            "token": token,
        },
        "status_code":200,
        "errors": []
    }

@router.get("/current-user")
def current_user():
    return {"message": "Weepul is current User"}
