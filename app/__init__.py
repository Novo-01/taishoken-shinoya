from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from app.views.main import main_bp
    app.register_blueprint(main_bp)

    return app
