import bcrypt


def encryptPass(password):
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def decryptPass(password, storagePassword):
    password = password.encode("utf-8")
    isSame = bcrypt.hashpw(password, password)
    print(isSame)
