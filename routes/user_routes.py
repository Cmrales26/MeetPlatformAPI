from flask import Blueprint, request
from controllers import user_controller


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/login", methods=["GET"])
def getUserRoute():
    return user_controller.Login()


@user_routes.route("/CreateAccount", methods=["POST"])
def createAccountRoute():
    data = request.json
    return user_controller.CreateAccount(data)
