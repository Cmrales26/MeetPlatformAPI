from flask import jsonify, request
from lib import lib
import uuid


# NOTE: if there is a request value call is Business the changes below will be added into the business table, otherwise it will be change in user table;
def CreateAccount(data):
    if "business" in data:
        # TODO: connection to database to insert the values into the business table
        if (
            "name" in data
            and data["name"].strip() != ""
            and "bio" in data
            and data["bio"].strip() != ""
            and "funationdate" in data
            and data["funationdate"].strip() != ""
            and "password" in data
            and data["password"].strip() != ""
        ):
            return jsonify({"message": "Business"}), 200
        else:
            return jsonify({"message": "Error"}), 400
    else:
        # TODO: connection to database to insert the values into the user table
        if (
            "name" in data
            and data["name"].strip() != ""
            and "lastname" in data
            and data["lastname"].strip() != ""
            and "bio" in data
            and data["bio"].strip() != ""
            and "birth" in data
            and data["birth"].strip() != ""
            and "email" in data
            and data["email"].strip() != ""
            and "phone" in data
            and data["phone"].strip() != ""
            and "password" in data
            and data["password"].strip() != ""
        ):
            hashed = lib.encryptPass(data["password"])

            newUser = {
                "id": str(uuid.uuid4()),
                "name": data["name"],
                "lastname": data["lastname"],
                "bio": data["bio"],
                "birth": data["birth"],
                "email": data["email"],
                "phone": data["phone"],
                "password": hashed.decode("utf-8"),
            }
            return jsonify(newUser)
        else:
            return jsonify({"message": "Error"}), 400


def Login():
    return jsonify({"message": "Login"}), 200


def LogOut():
    return jsonify({"message": "Logout"}), 200


def EditAcount():
    return jsonify({"message": "Edit"}), 200
