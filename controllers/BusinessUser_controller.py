from flask import jsonify, request, make_response
from db import queries_business
from lib import lib
import uuid


# NOTE: if there is a request value call is Business the changes below will be added into the business table, otherwise it will be change in user table;
def CreateAccount(data):
    required_fields = ["name", "bio", "fundationdate", "password"]

    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

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
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "Business Created"}), 201


def login(data):
    required_fields = ["name", "password"]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    business_found = queries_business.CheckBusinessUser(data["name"])

    print(business_found)

    # NOTE: if user not found
    if not business_found:
        return jsonify({"message": "Business not found"}), 404

    if business_found == "Disable":
        return jsonify({"message": "Business Disabled"}), 401

    # NOTE: if user found -> Check Pass
    check_pass = lib.decryptPass(data["password"], business_found["Password"])

    print(check_pass)

    if check_pass:
        payload = business_found
        payload.pop("Password", None)
        payload["rol"] = "business"
        token = lib.encodedJWT(payload)
        payload["token"] = token
        resp = make_response(jsonify(payload))
        resp.set_cookie("token", token)
        return resp
    else:
        return jsonify({"message": "Error"}), 401


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
    if updateRes == True:
        return jsonify({"message": "Business Updated"}), 200
    else:
        return jsonify({"message": "Error"}), 400


def DisableBusiness(id):
    check_business = queries_business.BusinessExists(id)
    if not check_business:
        return jsonify({"message": "Business not found"}), 404

    DisableRes = queries_business.DisableBusiness(id)
    if DisableRes == False:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "Business disable successfully"}), 200


def CreateEvent():
    return jsonify({"message": "Create Event"})


def editEvent():
    return jsonify({"message": "Edit Event"})


def deleteEvent():
    return jsonify({"message": "Delete Event"})
