from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..import schema,database,model
from sqlalchemy.orm import Session
from .import oauth2
router= APIRouter(
    prefix="/vote",
    tages=['vote']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def vote(vote:schema.Vote,db:Session=Depends(database.get_db),current_user:int=Depends(oauth2.get_current_user)):
    if(vote.dir==1):
        