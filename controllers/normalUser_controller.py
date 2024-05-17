from flask import jsonify, request, make_response
from db import queries
from lib import lib
import uuid


# 🟢
def CreateAccount(data):
    required_fields = [
        "name",
        "lastname",
        "bio",
        "birth",
        "email",
        "phone",
        "password",
    ]

    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    hashed = lib.encryptPass(data["password"])
    newUser = {
        "id": str(uuid.uuid4()),
        "name": data["name"].strip(),
        "lastname": data["lastname"].strip(),
        "bio": data["bio"].strip(),
        "birth": data["birth"].strip(),
        "email": data["email"].strip(),
        "phone": data["phone"].strip(),
        "password": hashed.decode("utf-8"),
    }
    createRes = queries.CreateNormalUser(newUser)

    if createRes == False:
        return jsonify({"message": "This Email is already Register"}), 400
    else:
        return jsonify({"message": "added"}), 201


# 🟢
def LoginUser(data):
    required_fields = ["email", "password"]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    user_found = queries.CheckNormalUser(data["email"])

    if not user_found:
        return jsonify({"message": "User not found"}), 404

    if user_found == "Disable":
        return jsonify({"message": "User Disabled"}), 401

    check_pass = lib.decryptPass(data["password"], user_found["Password"])

    if check_pass:
        payload = user_found
        payload.pop("Password", None)
        token = lib.encodedJWT(payload)
        payload["token"] = token
        resp = make_response(jsonify(payload))
        resp.set_cookie("token", token)
        return resp
    else:
        return jsonify({"message": "User Not found"}), 401


def UpdateUser(id, data):
    checkUser = queries.UserExists(id)
    if not checkUser:
        return jsonify({"message": "User not found"}), 404

    required_fields = ["name", "lastname", "bio", "birth", "phone"]

    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    newData = {
        "name": data["name"].strip(),
        "lastname": data["lastname"].strip(),
        "bio": data["bio"].strip(),
        "birth": data["birth"].strip(),
        "phone": data["phone"].strip(),
    }

    UpdateRes = queries.UpdateUser(id, newData)

    if UpdateRes == False:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "user update successfully"}), 200


def DisableUser(id):
    checkUser = queries.UserExists(id)
    if not checkUser:
        return jsonify({"message": "User not found"}), 404
    DisableRes = queries.DisableUser(id)
    if DisableRes == False:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "user disable successfully"}), 200
