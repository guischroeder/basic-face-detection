from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main import controller
    app.register_blueprint(controller.bp)
  
    return app
