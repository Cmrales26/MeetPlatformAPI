from flask import jsonify, request, make_response
from db import queries_events
from lib import lib
import uuid


def CreateEvent(data):
    # Check Token
    token = request.cookies.get("token")
    if not token:
        return jsonify({"message": "Error"}), 401

    tokenRES = lib.decodedJWT(token)

    if not tokenRES:
        return jsonify({"message": "Please Login"}), 401

    if not "rol" in tokenRES:
        return jsonify({"message": "You aren't a business"}), 401

    required_fields = [
        "name",
        "description",
        "date",
        "time",
        "location",
    ]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "Error"}), 400

    newEvent = {
        "id": str(uuid.uuid4()),
        "name": data["name"].strip(),
        "description": data["description"].strip(),
        "date": data["date"].strip(),
        "time": data["time"].strip(),
        "location": data["location"].strip(),
        "businessID": tokenRES["BusinessID"],
    }

    createRes = queries_events.CreateEvent(newEvent)
    if createRes == False:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "Event Created"}), 201
