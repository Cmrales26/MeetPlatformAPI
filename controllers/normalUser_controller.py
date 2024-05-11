from flask import jsonify


def JointEvent():
    return jsonify({"message": "JointEvent"}), 200


def QuitEvent():
    return jsonify({"message": "QuitEvent"}), 200
