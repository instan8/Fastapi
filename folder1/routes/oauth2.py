from jose import JWTError,jwt
from datetime import datetime,timedelta
from ..import schema

from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
print(oauth2_scheme)
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire= datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credentials_exception):
      try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id=payload.get("user_id")
        print("id",type(id))
        if id is None:
            raise credentials_exception
        token_data=schema.TokenData(id=id) 
        print("this is token_data",token_data)   
      except JWTError:
        raise credentials_exception  
      return token_data  

def get_current_user(token:str=Depends(oauth2_scheme)):
          print(token)
          print(oauth2_scheme)
          print('get_current_user')
          credential_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="could not find",headers={"WWW-Authenticate":"Bearer"})
          return verify_access_token(token,credential_exception)
