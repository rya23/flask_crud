from flask import Flask, json, jsonify
from flask_pymongo import PyMongo
import os
from flask.cli import load_dotenv
from bson import json_util


load_dotenv()
mongo = PyMongo()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        MONGO_URI=os.getenv("MONGO_URI"),
    )
    mongo.init_app(app)
    from app.routes import user_bp

    app.register_blueprint(user_bp)

    @app.route("/")
    def api():
        return "Hello"

    return app
