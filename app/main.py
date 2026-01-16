from flask import Flask
from app.api.enhance_api import enhance_api
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(enhance_api)
    return app
