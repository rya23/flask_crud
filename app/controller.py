from app import mongo
from bson import ObjectId
from flask import json, jsonify


class UserController:

    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        return list(users)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = mongo.db.users.find_one_or_404({"_id": ObjectId(user_id)})
            return user
        except Exception as e:
            return None

    @staticmethod
    def create_user(data):
        try:
            user_id = mongo.db.users.insert_one(data).inserted_id
            new_user = mongo.db.users.find_one({"_id": user_id})
            return new_user
        except Exception as e:
            return None

    @staticmethod
    def update_user(user_id, data):
        try:

            mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})
            updated_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            return updated_user
        except Exception as e:
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            response = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
            return response
        except Exception as e:
            return None
