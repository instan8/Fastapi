from pydantic import BaseModel,EmailStr,conint
from datetime import datetime
import time
from typing import Optional

from sqlalchemy.sql.sqltypes import TIMESTAMP
class Post(BaseModel):
    title:str
    content:str
    published:bool

class RetType(Post):
  id:int
  owner_id:int
  class Config:
    orm_mode=True    


class UserCreate(BaseModel):
    firstname:str
    lastname:str
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
     orm_mode=True    
class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class  TokenData(BaseModel):
    id:Optional[str] = None


class Vote(BaseModel):
    post_id:int
    dir:conint(ge=0,le=1)