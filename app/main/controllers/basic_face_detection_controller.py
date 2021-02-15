from flask import Blueprint

basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.route("/", methods=["GET"])
def get():
    return "Hello!"
