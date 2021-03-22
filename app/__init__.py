from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main.controller import basic_face_detection_bp

    app.register_blueprint(basic_face_detection_bp)

    return app
