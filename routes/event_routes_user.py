from flask import Flask, jsonify, Blueprint, request
from controllers.events.user_events import events_Controller

User_events_routes = Blueprint("User_events_routes", __name__)


@User_events_routes.route("/get/events")
def getAllEvents():
    return events_Controller.get_events()


@User_events_routes.route("/get/event/<EvenID>")
def getEvent(EvenID):
    return events_Controller.get_event(EvenID)


@User_events_routes.route("/join/event", methods=["POST"])
def JoinEvent():
    data = request.json
    return events_Controller.JoinEvent(data)


@User_events_routes.route("/leave/event", methods=["POST"])
def LeaveEvent():
    data = request.json
    return events_Controller.LeaveEvent(data)
