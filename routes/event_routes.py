from flask import Flask, jsonify, Blueprint, request
from controllers.events.Business_events import events_Controller

event_routes = Blueprint("event_routes", __name__)


@event_routes.route("/Business/my/events")
def getEventsRoute():
    return events_Controller.get_events()


@event_routes.route("/create/event", methods=["POST"])
def CreateEventRoute():
    data = request.json
    return events_Controller.CreateEvent(data)


@event_routes.route("/update/event/<EventID>", methods=["PATCH"])
def UpdateEventRoute(EventID):
    id = EventID
    data = request.json
    return events_Controller.editEvent(id, data)


@event_routes.route("/delete/event/<EventID>", methods=["DELETE"])
def DeleteEventRoute(EventID):
    id = EventID
    return events_Controller.delete_event(id)


@event_routes.route("/Business/my/event/<EventID>", methods=["GET"])
def GetEventRoute(EventID):
    id = EventID
    return events_Controller.get_event(id)
