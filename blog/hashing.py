from base64 import encode
import bcrypt
from passlib.context import CryptContext


class Hash():
    def bcrypt(password: str):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    
    def verify(user_password, request_password):
        return bcrypt.checkpw(request_password.encode('utf8'), user_password)