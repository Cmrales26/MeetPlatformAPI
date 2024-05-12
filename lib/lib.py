import bcrypt
import jwt
import os
from dotenv import load_dotenv

load_dotenv()


def encryptPass(password):
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def decryptPass(password, storagePassword):
    password = password.encode("utf-8")
    storagePassword = storagePassword.encode("utf-8")
    isSame = bcrypt.checkpw(password, storagePassword)
    return isSame


def encodedJWT(payload):
    secret = os.getenv("SECRET", "secret")
    encodedJWT = jwt.encode(payload, secret, algorithm="HS256")
    return encodedJWT
