from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from ..import schema
from .. getDb import get_db
from .. import model
from ..import hashing
from .import oauth2

router=APIRouter()

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(model.User).filter(model.User.email==user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="invalid credentials")
    if not hashing.verify(user_credentials.password,user.password)  :
          raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials"
          )
    access_token=oauth2.create_access_token(data={"user_id":user.id})     
    return {"token":access_token,"token_type":"bearer"}      
    
