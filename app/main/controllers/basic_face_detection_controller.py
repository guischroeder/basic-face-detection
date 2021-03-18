import os

from flask import Blueprint
from app.settings import Settings
from app.main.clients.aws_client import AWSClient
from app.main.services.hackattic_service import HackatticService
from app.main.services.s3_service import S3Service
from app.main.utils.handle_error import handle_error


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/solve", methods=["GET"])
def get():
    s3_client = AWSClient(
        aws_service="s3",
        region_name="us-west-1",
        credentials=Settings.aws_s3_credentials(),
    )

    image_url = HackatticService(Settings.hackattic_credentials()).get_image_url()

    return S3Service(s3_client).upload_image_from_url(
        image_url, os.getenv("S3_BUCKET"), "media/faces.jpg"
    )
