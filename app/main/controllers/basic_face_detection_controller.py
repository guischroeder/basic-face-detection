import os

from flask import Blueprint
from app.settings import Settings
from app.main.utils.handle_error import handle_error
from app.main.services.hackattic_service import HackatticService
from app.main.services.s3_service import S3Service


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/problem", methods=["GET"])
def get():
    image_url = HackatticService(Settings.hackattic_credentials()).get_image_url()
    return S3Service(Settings.aws_s3_credentials()).upload_image_from_url(
        image_url, os.getenv("S3_BUCKET"), "media/faces.jpg"
    )
