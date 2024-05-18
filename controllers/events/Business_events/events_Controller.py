from flask import jsonify, request, make_response
from db import queries_events
from lib import lib
import uuid


# 🟢
def get_events():
    # Validate Token
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"message": "Missing authorization header"}), 401

    token = auth_header.split()[1]
    TokenRes = lib.TokenBusiness(token)
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    BusinessID = TokenRes["Business"]["BusinessID"]

    Events = queries_events.Get_Event(BusinessID)
    if not Events:
        return jsonify({"message": "Events not found"}), 404

    return Events


def get_event(id):
    # Validate Token
    TokenRes = lib.TokenBusiness()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    BusinessID = TokenRes["Business"]["BusinessID"]

    Event = queries_events.Get_Event_by_id(id, BusinessID)

    if not Event:
        return jsonify({"message": "Event not found"}), 404

    return Event


# 🟢
def CreateEvent(data):
    # Validate Token
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"message": "Missing authorization header"}), 401

    token = auth_header.split()[1]
    TokenRes = lib.TokenBusiness(token)
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    required_fields = [
        "name",
        "description",
        "date",
        "time",
        "location",
    ]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "There are Empty spaces"}), 400

    newEvent = {
        "id": str(uuid.uuid4()),
        "name": data["name"].strip(),
        "description": data["description"].strip(),
        "date": data["date"].strip(),
        "time": data["time"].strip(),
        "location": data["location"].strip(),
        "businessID": TokenRes["Business"]["BusinessID"],
    }

    createRes = queries_events.CreateEvent(newEvent)
    if createRes == False:
        return jsonify({"message": "Error in DB"}), 400

    return jsonify({"message": "Event Created"}), 201


def editEvent(id, data):
    # Validate Token
    TokenRes = lib.TokenBusiness()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    # Validate Event and Event Creator

    BusinessId = TokenRes["Business"]["BusinessID"]

    CanEdit = queries_events.validate_event_permission(BusinessId, id)

    if not CanEdit:
        return jsonify({"message": "You can't edit this event"}), 401

    required_fields = [
        "name",
        "description",
        "date",
        "time",
        "location",
    ]
    if not all(data.get(field, "").strip() for field in required_fields):
        return jsonify({"message": "There are Empty spaces"}), 400

    newEvent = {
        "name": data["name"].strip(),
        "description": data["description"].strip(),
        "date": data["date"].strip(),
        "time": data["time"].strip(),
        "location": data["location"].strip(),
    }
    updateRES = queries_events.update_event(id, newEvent)
    if not updateRES:
        return jsonify({"message": "Error in DB"}), 400

    return jsonify({"message": "Update Success"}), 200


def delete_event(id):
    TokenRes = lib.TokenBusiness()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    # Validate Event and Event Creator

    BusinessId = TokenRes["Business"]["BusinessID"]

    CanDelete = queries_events.validate_event_permission(BusinessId, id)

    if not CanDelete:
        return jsonify({"message": "You can't delete this event"}), 401

    DeleteRES = queries_events.delete_event(id)
    if not DeleteRES:
        return jsonify({"message": "Error in DB"}), 400

    return jsonify({"message": "Delete"}), 200
