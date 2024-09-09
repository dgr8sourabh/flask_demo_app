from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from datetime import timedelta
import os


jwt = JWTManager()


def create_app():
    app = (
        Flask(__name__))

    from .routes import homepage
    app.register_blueprint(homepage.homepage_bp)

    return app
