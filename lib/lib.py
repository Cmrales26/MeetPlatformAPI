import bcrypt
import jwt
import os
from dotenv import load_dotenv
from flask import jsonify, request

load_dotenv()
secret = os.getenv("SECRET", "secret")


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
    encodedJWT = jwt.encode(payload, secret, algorithm="HS256")
    return encodedJWT


def decodedJWT(Token):
    decodedJWT = jwt.decode(Token, secret, algorithms=["HS256"])
    return decodedJWT


def TokenBusiness():
    token = request.cookies.get("token")
    if not token:
        return {"message": "Please Login", "Status": False}

    tokenRES = decodedJWT(token)

    if not tokenRES:
        return {"message": "Please Login", "Status": False}

    if not "rol" in tokenRES:
        return {"message": "You aren't a business", "Status": False}

    return {"Business": tokenRES, "Status": True}


def TokenUser():
    token = request.cookies.get("token")
    if not token:
        return {"message": "Please Login", "Status": False}

    tokenRES = decodedJWT(token)

    if not tokenRES:
        return {"message": "Please Login", "Status": False}

    return {"User": tokenRES, "Status": True}
