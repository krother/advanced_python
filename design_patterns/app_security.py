"""
pip install python-multipart

uvicorn --reload app:app

source: https://fastapi.tiangolo.com/tutorial/security/first-steps

TODO: add JWT tokens and encryption with https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
"""
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel  

user_db = {
    "ada": {
        "username": "ada",
        "full_name": "Ada Lovelace",
        "email": "ada@byron.co.uk",
        "hashed_password": "fake_bernoulli",
        "disabled": False,
    },
    "alan": {
        "username": "alan",
        "full_name": "Alan Turing",
        "email": "turing@plete.com",
        "hashed_password": "fake_enigma",
        "disabled": True,
    },
}
app = FastAPI()

def fake_hash_password(password: str):
    return "fake_" + password

# define URL to login with user+psw to receive bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(user_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = user_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/userinfo")
async def read_usersinfo(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user