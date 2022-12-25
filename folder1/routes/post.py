
from .. import schema 
from .. hashing import hasher
from typing import List
from .. import model
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.security import oauth2
from .import oauth2
from sqlalchemy.orm import Session 
from ..getDb import get_db
from sqlalchemy import func
router=APIRouter()
@router.get("/allPosts",)
async def root(db: Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM post""")
    # posts=cursor.fetchall()
   print("user",get_current_user)
   posts=db.query(model.Post).all()
   return{"data":posts}

# @router.get("/latest_post")
# def latest_post():
#     return {"mypost":mypost[len(mypost)-1]}
# def post(payload: dict= Body(...)):
#     print(payload)
#     return{"message":"succes"}

@router.post("/post",response_model=schema.RetType)
def posts(post:schema.Post,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO post (title ,content,published) VALUES (%s, %s , %s)""",(post.title,post.content,post.published))
    # conn.commit()
    print("hello",current_user.id)
   
    new_post=model.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print("the new post is",new_post)
    return new_post

# @app.get("/post/{id}")
# def post(id:int,response:Response):
#  for post in mypost:
#     if(post["id"]==id):
#         return{"data":post}
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id = {id} not found")
@router.get("/post/{id}")
def post(id:int,db: Session = Depends(get_db)):
 
  post=db.query(model.Post).filter(model.Post.id==id).first()
  if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id = {id} not found")
  else:
    return{"post":post}      
       
@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delet_post(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # for i,p in enumerate(mypost):
    #     if(p["id"]==id):
    #         mypost.pop(i)
    #         print(mypost)
    #         return{"message":"post deleted"}
    post=db.query(model.Post).filter(model.Post.id==id)     

    if post.first()== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id = {id} not found")
    elif post.first().owner_id !=current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,detail="not admin"
        )
    else:
        post.delete(synchronize_session=False)
        db.commit()


@router.put("/update/{id}")
def update_post(id:int,Updated_post:schema.Post,db: Session = Depends(get_db)):
    post_query=db.query(model.Post).filter(model.Post.id==id)
    post=post_query.first()

    if post==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id = {id} not found")
    post_query.update(Updated_post.dict(),synchronize_session=False)    
    db.commit() 

@router.get("/vote/{id}")
def getPost(id:int,db:Session =Depends(get_db)):
    Post=db.query(model.Post,func.count(model.Vote.post_id).label("votes")).join(model.Vote,model.Vote.post_id==model.Post.id,isouter=True).group_by(model.Post.id)
    print(Post)
    Post=Post.all()
    print(Post)
    return {"post":Post}
   