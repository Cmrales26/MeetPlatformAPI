from flask import jsonify, make_response


def LogOut():
    resp = make_response(jsonify({"message": "LogOut"}), 200)
    resp.set_cookie("token", "", expires=0)
    return resp
