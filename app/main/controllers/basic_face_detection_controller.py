from flask import Blueprint
from app.main.services.hackattic_service import HackatticService
from app.settings import Settings


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.route("/problem", methods=["GET"])
def get():
    return HackatticService(Settings.hackattic_credentials()).get_problem()
