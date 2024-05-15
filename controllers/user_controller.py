from flask import jsonify, make_response, request
from lib import lib


def LogOut():
    resp = make_response(jsonify({"message": "LogOut"}), 200)
    resp.set_cookie("token", "", expires=0)
    return resp


def CheckLogin(token):
    token = token["token"]
    if not token:
        return jsonify({"message": "Please Login"}), 401

    tokenRES = lib.decodedJWT(token)
    if not tokenRES:
        return jsonify({"message": "Please Login"}), 401

    return tokenRES
