from pydantic import BaseModel, EmailStr
from typing import Optional, List

from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "user-email@email.com",
                "password": "userPassword",
                "username": "userName",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "user-email@email.com",
                "password": "userPassword",
            }
        }