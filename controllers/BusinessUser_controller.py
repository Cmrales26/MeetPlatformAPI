from flask import jsonify


def CreateEvent():
    return jsonify({"message": "Create Event"})


def editEvent():
    return jsonify({"message": "Edit Event"})


def deleteEvent():
    return jsonify({"message": "Delete Event"})
