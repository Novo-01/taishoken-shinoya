from flask import Flask
import os

def create_app():
    template_dir = os.path.abspath('templates')  # 明示的に指定！
    app = Flask(__name__, template_folder=template_dir)

    from app.views.main import main_bp
    app.register_blueprint(main_bp)

    return app
