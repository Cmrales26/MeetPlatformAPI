from flask import Blueprint
from controllers import user_controller


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/user", methods=["GET"])
def getUserRoute():
    return user_controller.getUser()
