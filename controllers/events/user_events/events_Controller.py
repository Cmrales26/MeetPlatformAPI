from flask import jsonify, request, make_response
from db import queries_events_users
from lib import lib
import uuid


def get_events():
    TokenRes = lib.TokenUser()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    Events = queries_events_users.Get_Events()
    if len(Events) == 0:
        return jsonify({"message": "No events"}), 404

    return Events


def get_event(id):
    TokenRes = lib.TokenUser()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    Event = queries_events_users.Get_Event(id)

    if len(Event) == 0:
        return jsonify({"message": "Event not found"}), 404

    userID = TokenRes["User"]["UserID"]
    Check_user_in_event = queries_events_users.Check_user_in_event(userID, id)
    print(Check_user_in_event)
    if not Check_user_in_event:
        Event[0]["UserInEvent"] = False
    else:
        Event[0]["UserInEvent"] = True

    return Event


def JoinEvent(EventId):
    TokenRes = lib.TokenUser()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401

    eventExists = queries_events_users.Get_Event(EventId["EventID"])
    if len(eventExists) == 0:
        return jsonify({"message": "Event not found"}), 404

    userID = TokenRes["User"]["UserID"]
    EventID = EventId["EventID"]

    JoinEventRes = queries_events_users.JoinEvent(userID, EventID)

    if not JoinEventRes:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "User joined"}), 200


def LeaveEvent(EventId):
    TokenRes = lib.TokenUser()
    if not TokenRes["Status"]:
        return jsonify({"message": TokenRes["message"]}), 401
    eventExists = queries_events_users.Get_Event(EventId["EventID"])
    if len(eventExists) == 0:
        return jsonify({"message": "Event not found"}), 404
    userID = TokenRes["User"]["UserID"]
    EventID = EventId["EventID"]

    Check_user_in_event = queries_events_users.Check_user_in_event(userID, EventID)

    if not Check_user_in_event:
        return jsonify({"message": "Not in the event"}), 400

    LeaveEventRes = queries_events_users.LeaveEvent(userID, EventID)

    if not LeaveEventRes:
        return jsonify({"message": "Error"}), 400

    return jsonify({"message": "User left"}), 200
