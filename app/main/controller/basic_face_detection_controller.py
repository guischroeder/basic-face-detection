from flask import Blueprint

from app.main.libs.hackattic.hackattic_client import HackatticClient
from app.main.libs.aws.aws_client import AWSClient
from app.main.libs.aws.s3.s3_service import S3Service
from app.main.libs.aws.rekognition.rekognition_service import RekognitionService
from app.main.utils.handle_error import handle_error
from app.main.config import config


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/solve", methods=["GET"])
def get():
    hackattic_client = HackatticClient(config["hackattic"])
    s3_client = AWSClient(aws_service="s3", config=config["s3"])
    rekognition_client = AWSClient(
        aws_service="rekognition", config=config["rekognition"]
    )

    s3_service = S3Service(s3_client)
    rekognition_service = RekognitionService(rekognition_client)

    BUCKET_NAME = "basic-face-detection"
    IMAGE_PATH = "media/faces.jpg"

    s3_service.upload_image_from_url(
        image_url=hackattic_client.get_problem().get("image_url", ""),
        bucket_name=BUCKET_NAME,
        image_path=IMAGE_PATH,
    )

    return rekognition_service.detect_faces(
        bucket_name=BUCKET_NAME, image_path=IMAGE_PATH,
    )
