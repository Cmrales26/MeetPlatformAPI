from flask import Blueprint, request, jsonify
from controllers import BusinessUser_controller

business_routes = Blueprint("business_routes", __name__)


@business_routes.route("/create/business", methods=["POST"])
def CreateAccountRoute():
    data = request.json
    return BusinessUser_controller.CreateAccount(data)


@business_routes.route("/login/business", methods=["POST"])
def LoginBusinessRoute():
    data = request.json
    return BusinessUser_controller.login(data)


@business_routes.route("/edit/business/<BusinessID>", methods=["PATCH"])
def editBusinessRoute(BusinessID):
    id = BusinessID
    data = request.json
    return BusinessUser_controller.updateBusiness(id, data)


@business_routes.route("/disable/business/<BusinessID>", methods=["POST"])
def disableBusinessRoute(BusinessID):
    id = BusinessID
    return BusinessUser_controller.DisableBusiness(id)


@business_routes.route("/change/pass/business", methods=["POST"])
def changeBusinessPass():
    data = request.json
    return BusinessUser_controller.ChangePassB(data)


# TODO: Enable Business
