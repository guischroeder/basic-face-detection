from flask import Blueprint, jsonify

from app.main.libs.hackattic.hackattic_client import HackatticClient
from app.main.libs.aws.aws_client import AWSClient
from app.main.libs.aws.s3_service import S3Service
from app.main.libs.aws.rekognition_service import RekognitionService
from app.main.libs.face_detection.positions_service import PositionsService
from app.main.utils.handle_error import handle_error
from app.main.config import config
from app.main.general import BUCKET_NAME, IMAGE_PATH


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
    position_service = PositionsService()

    s3_service.upload_image_from_url(
        image_url=hackattic_client.get_problem().get("image_url", ""),
        bucket_name=BUCKET_NAME,
        image_path=IMAGE_PATH,
    )

    faces = rekognition_service.detect_faces(
        bucket_name=BUCKET_NAME, image_path=IMAGE_PATH,
    )

    positions = position_service.find_positions(faces)

    return hackattic_client.solve(positions)
