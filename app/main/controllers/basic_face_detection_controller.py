from flask import Blueprint

from app.main.clients.aws.rekognition.rekognition_client import RekognitionClient
from app.main.services.rekognition_service import RekognitionService
from app.settings import Settings
from app.main.clients.hackattic.hackattic_client import HackatticClient
from app.main.clients.aws.s3.s3_client import S3Client
from app.main.services.s3_service import S3Service
from app.main.utils.handle_error import handle_error


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/solve", methods=["GET"])
def get():
    hackattic_client = HackatticClient(Settings.hackattic_access_token())

    bucket_settings = Settings.s3_bucket()
    s3_client = S3Client(
        credentials=Settings.s3_credentials(), region_name=bucket_settings["region"]
    )

    rekognition_client = RekognitionClient(
        credentials=Settings.rekognition_credentials(),
        region_name=Settings.rekognition_service_region(),
    )

    s3_service = S3Service(s3_client)
    s3_service.upload_image_from_url(
        image_url=hackattic_client.get_problem().get("image_url", ""),
        bucket=bucket_settings["name"],
        key=bucket_settings["key"],
    )

    rekognition_service = RekognitionService(rekognition_client)
    return rekognition_service.detect_faces(
        bucket=bucket_settings["name"], key=bucket_settings["key"],
    )
