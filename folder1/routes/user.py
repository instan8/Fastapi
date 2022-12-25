
from .. import schema 
from .. hashing import hasher
from .. import model
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session 
from ..getDb import get_db
router=APIRouter()
from fastapi import FastAPI, Form

app = FastAPI()


# @app.post("/login/")
# async def login(username: str = Form(), password: str = Form()):
#     return {"username": username}

@router.post("/register",response_model=schema.UserOut)
async def register(firstname: str = Form(),lastname=Form(),email=Form(), password: str = Form(),db: Session = Depends(get_db)):
   password=hasher(password)
   values={"name":firstname+lastname,"email":email,"password" :password}
   new_post={}
   new_post.update(values)
   database_user=model.User(**new_post)
   db.add(database_user)
   db.commit()
   db.refresh(database_user)
   print(database_user)
   return database_user

# Routing

@router.get('/users/{id}')
def get_user(id:int , db: Session = Depends(get_db)):
    pass
 