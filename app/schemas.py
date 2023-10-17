from datetime import date

from typing import List
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    id :int
    accessToken:str
    token_type: str
    email:EmailStr
    role:str
    phone:str
    name:str
    

class TokenData(BaseModel):
    id:int


class UserSignup(BaseModel):
    email:EmailStr
    password:str
    name:str
    phone:str


class UserOut(BaseModel):
    id:int
    email:EmailStr
    name:str
    phone:str
    role : str

class UserSignin(BaseModel):
    email:EmailStr
    password:str

class TeacherSingnUp(BaseModel):

    user :UserSignup
    bio : str
    subject:str
    currentInstitution:str
    offlineFee:int
    onlineFee:int

    class Config:
        orm_mode = True


class TeacherOut(BaseModel):
    user : UserOut
    bio : str
    subject : str
    currentInstitution : str
    offlineFee : int
    onlineFee : int
    rating : float
    user : UserOut

    class Config:
        orm_mode = True



