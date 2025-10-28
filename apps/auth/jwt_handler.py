import jwt
from datetime import datetime, timedelta
from config.settings import get_settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .repository import AuthRepository
from sqlmodel import Session
from config.database import get_session


SECRET_KEY = get_settings().SECRET_KEY
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def generate_jwt_token(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + ( timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt)
    return encoded_jwt

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


def get_current_user(token:str = Depends(oauth2_scheme),session: Session = Depends(get_session) ):
    try:

        payload = verify_jwt_token(token)
        user_email=payload.get("email",None)
        if user_email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user not found")

        repo = AuthRepository(session=session)
        user=repo.get_user_by_email(user_email)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
        current_user=user.model_dump()
        return current_user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")

    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid user")




