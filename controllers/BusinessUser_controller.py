from flask import jsonify, request, make_response
from db import queries_business
from lib import lib
import uuid


# 🟢
def CreateAccount(data):
    required_fields = ["name", "bio", "fundationdate", "password"]

    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "faltandatos"}), 400

    hashed = lib.encryptPass(data["password"])
    newBusiness = {
        "id": str(uuid.uuid4()),
        "name": data["name"].strip(),
        "bio": data["bio"].strip(),
        "fundationdate": data["fundationdate"].strip(),
        "password": hashed.decode("utf-8"),
    }
    CreateRes = queries_business.CreateBusiness(newBusiness)
    print(CreateRes)
    if CreateRes == False:
        return jsonify({"message": "This Business is already registered"}), 400

    return jsonify({"message": "Business Created"}), 201


# 🟢
def login(data):
    required_fields = ["name", "password"]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    business_found = queries_business.CheckBusinessUser(data["name"])

    # NOTE: if user not found
    if not business_found:
        return jsonify({"message": "Business not found"}), 404

    if business_found == "Disable":
        return jsonify({"message": "Business Disabled"}), 401

    # NOTE: if user found -> Check Pass
    check_pass = lib.decryptPass(data["password"], business_found["Password"])

    if check_pass:
        payload = business_found
        payload.pop("Password", None)
        payload["rol"] = "business"
        token = lib.encodedJWT(payload)
        payload["token"] = token
        resp = make_response(jsonify(payload))
        return resp
    else:
        return jsonify({"message": "Business Not Found"}), 401


# 🟢
def updateBusiness(id, data):
    check_business = queries_business.BusinessExists(id)
    if not check_business:
        return jsonify({"message": "Business not found"}), 404

    required_fields = ["bio", "fundationdate"]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    newBusiness = {
        "bio": data["bio"].strip(),
        "fundationdate": data["fundationdate"].strip(),
    }
    updateRes = queries_business.UpdateBusiness(newBusiness, id)

    if updateRes == False:
        return jsonify({"message": "Error"}), 400

    Business_Found = queries_business.CheckBusinessUser(data["name"])

    if not Business_Found:
        return jsonify({"message": "Business not found"}), 404

    payload = Business_Found
    payload.pop("Password", None)
    payload["rol"] = "business"
    token = lib.encodedJWT(payload)
    return jsonify({"message": "Business update successfully", "token": token}), 200


# Not usable yet
def DisableBusiness(id):
    check_business = queries_business.BusinessExists(id)
    if not check_business:
        return jsonify({"message": "Business not found"}), 404

    DisableRes = queries_business.DisableBusiness(id)
    if DisableRes == False:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "Business disable successfully"}), 200


# 🟢
def ChangePassB(data):
    Business_Found = queries_business.CheckBusinessUser(data["name"])
    # print(Business_Found)
    if not Business_Found:
        return jsonify({"message": "Business not found"}), 404

    check_pass = lib.decryptPass(data["password"], Business_Found["Password"])
    if not check_pass:
        return jsonify({"message": "Incorrect password"}), 401

    hashed = lib.encryptPass(data["newPassword"])
    UpdateRes = queries_business.ChangePasswordB(
        data["name"],
        hashed.decode("utf-8"),
    )
    if not UpdateRes:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "Password change successfully"}), 200
