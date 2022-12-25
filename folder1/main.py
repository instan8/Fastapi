from typing import Optional
import time
from passlib.context import CryptContext
from sqlalchemy.orm import Session 
from fastapi import FastAPI,Response,status,HTTPException,Depends
from .import schema
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from . hashing import hasher
from psycopg2.extras import RealDictCursor
from .import model
from . database import engine,SessionLocal
model. Base.metadata.create_all(bind=engine)
from .routes import post,user,auth,images
from .Config import settings
from fastapi.middleware.cors import CORSMiddleware



# connection
# try:
#     conn= psycopg2.connect(host=settings.database_hostname,database=settings.database_name,user=settings.database_username,password=settings.database_password,cursor_factory=RealDictCursor)
#     cursor=conn.cursor()
#     print("connected")
# except Exception as error:
#     print("connection is failed")
#     print("error",error)

origins=["http://localhost:3000"]
app=FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(images.router)
    # rating:Optional[int]=None



# registration

