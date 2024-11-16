from flask import Blueprint, json, jsonify, request, Response

from app.controller import UserController
from app.models import User
from pydantic import ValidationError
from bson import json_util

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/", methods=["GET"])
def get_users():
    all_users = UserController.get_all_users()
    return Response(json_util.dumps(all_users), mimetype="application/json")


@user_bp.route("/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = UserController.get_user_by_id(user_id)

    if user:
        return Response(json_util.dumps(user), mimetype="application/json")
    return jsonify({"error": "User not found"}), 404


@user_bp.route("/", methods=["POST"])
def create_user():
    try:
        data = request.json
        user = User(**request.get_json())
        created_user = UserController.create_user(user.to_dict())
        return Response(json_util.dumps(created_user), mimetype="application/json")
    except ValidationError as e:
        return jsonify(e.errors()), 400


@user_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        data = request.json
        updated_user = UserController.update_user(user_id, data)
        if updated_user:
            return Response(json_util.dumps(updated_user), mimetype="application/json")
        return jsonify({"error": "User not found"}), 404
    except ValidationError as e:
        return jsonify(e.errors()), 400


@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):

    response = UserController.delete_user(user_id)
    if response:
        if response.deleted_count == 1:
            return {"message": "User Deleted"}
    return {"message": "User not found"}, 404
