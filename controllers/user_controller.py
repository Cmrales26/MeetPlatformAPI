from flask import jsonify, request


def getUser():
    return jsonify({"message": "hello"}), 200
