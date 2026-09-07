import app.model.user_model as repository
from dotenv import find_dotenv, load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from ..schema.user_schema import User
from typing import Annotated

load_dotenv(find_dotenv())

ALGORITHM: str = os.getenv("ALGORITHM", "")
SECRET_KEY: str = os.getenv("SECRET_KEY", "")

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = repository.find_by_username(username)
    if user is None:
        raise credentials_exception
    return User(**user)
