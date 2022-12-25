from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
def hasher(password):
   return  pwd_context.hash(password)

def verify(plain_password,hashed_password):
   ret=pwd_context.verify(plain_password,hashed_password)
   print("the verify password",ret)
   return ret