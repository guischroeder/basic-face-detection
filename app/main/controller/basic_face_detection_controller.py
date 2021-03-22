from flask import Blueprint

from app.main.libs.hackattic.hackattic_client import HackatticClient
from app.main.libs.aws.aws_client import AWSClient
from app.main.libs.aws.s3.s3_service import S3Service
from app.main.libs.aws.rekognition.rekognition_service import RekognitionService
from app.main.utils.handle_error import handle_error
from app.settings import Settings


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/solve", methods=["GET"])
def get():
    hackattic_client = HackatticClient(Settings.hackattic_access_token())
    s3_client = AWSClient(
        aws_service="s3",
        credentials=Settings.s3_credentials(),
        region_name=Settings.s3_service_region(),
    )
    rekognition_client = AWSClient(
        aws_service="rekognition",
        credentials=Settings.rekognition_credentials(),
        region_name=Settings.rekognition_service_region(),
    )

    s3_service = S3Service(s3_client)
    rekognition_service = RekognitionService(rekognition_client)

    s3_service.upload_image_from_url(
        image_url=hackattic_client.get_problem().get("image_url", ""),
        bucket_name=Settings.s3_bucket_name(),
        key=Settings.s3_bucket_image_path(),
    )

    return rekognition_service.detect_faces(
        bucket_name=Settings.s3_bucket_name(), key=Settings.s3_bucket_image_path(),
    )
