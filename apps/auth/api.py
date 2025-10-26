from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user():
    return {"message": "successfully registered"}

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
