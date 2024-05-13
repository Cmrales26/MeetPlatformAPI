from flask import Flask, jsonify, Blueprint, request
from controllers.events.Business_events import Business_events

event_routes = Blueprint("event_routes", __name__)


@event_routes.route("/events")
def getEventsRoute():
    return jsonify({"message": "Events"})


@event_routes.route("/create/event", methods=["POST"])
def CreateEventRoute():
    data = request.json
    return Business_events.CreateEvent(data)


@event_routes.route("/update/event/<EventID>", methods=["PATCH"])
def UpdateEventRoute(EventID):
    id = EventID
    data = request.json
    return Event_controller.UpdateEvent(id, data)


@event_routes.route("/delete/event/<EventID>", methods=["DELETE"])
def DeleteEventRoute(EventID):
    id = EventID
    return Event_controller.DeleteEvent(id)


@event_routes.route("/event/<EventID>", methods=["GET"])
def GetEventRoute(EventID):
    id = EventID
    return Event_controller.GetEvent(id)
