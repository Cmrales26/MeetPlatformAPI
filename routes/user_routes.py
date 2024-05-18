from flask import Blueprint, request, jsonify
from controllers import user_controller, normalUser_controller


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/login/user", methods=["POST"])
def LoginUserRoute():
    data = request.json
    return normalUser_controller.LoginUser(data)


@user_routes.route("/CreateAccount/user", methods=["POST"])
def createAccountRoute():
    data = request.json
    return normalUser_controller.CreateAccount(data)


@user_routes.route("/edit/user/<UserID>", methods=["PATCH"])
def editUserRoute(UserID):
    id = UserID
    data = request.json
    return normalUser_controller.UpdateUser(id, data)


@user_routes.route("/change/user/pass", methods=["POST"])
def changePassRoute():
    data = request.json
    return normalUser_controller.ChangePass(data)


# AUTH
@user_routes.route("/logout", methods=["GET"])
def logoutRoute():
    return user_controller.LogOut()


@user_routes.route("/checkLogin", methods=["POST"])
def checkLoginRoute():
    token = request.json
    return user_controller.CheckLogin(token)
