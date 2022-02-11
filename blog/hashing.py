import bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    def verify(user_password, request_password):
        hashed_pass = pwd_context.hash(request_password)
        print(bcrypt.checkpw(request_password.encode('utf-8'), user_password))
        return user_password == hashed_pass
        