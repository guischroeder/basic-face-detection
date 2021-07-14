from flask import Blueprint, send_file

from app.libs.hackattic.hackattic_service import HackatticService
from app.libs.aws.aws_client import AWSClient
from app.libs.aws.s3_service import S3Service
from app.libs.aws.rekognition_service import RekognitionService
from app.libs.face_detection.positions_service import PositionsService
from app.libs.face_detection.image_service import ImageService
from app.libs.face_detection.face_detection_facade import FaceDetectionFacade
from app.handle_error import handle_error
from app.config import config


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/basic-face-detection/solve", methods=["GET"])
def get():
    s3_client = AWSClient(aws_service="s3", config=config["s3"])
    rekognition_client = AWSClient(
        aws_service="rekognition", config=config["rekognition"]
    )

    hackattic_service = HackatticService(config["hackattic"])
    s3_service = S3Service(s3_client)
    rekognition_service = RekognitionService(rekognition_client)
    positions_service = PositionsService()
    image_service = ImageService(
        positions_service=positions_service, s3_service=s3_service
    )

    face_detection_facade = FaceDetectionFacade(
        hackattic_service=hackattic_service,
        s3_service=s3_service,
        rekognition_service=rekognition_service,
        positions_service=positions_service,
        image_service=image_service,
    )

    face_detection_facade.solve_problem()

    recognited_image = face_detection_facade.show_detected_faces()

    return send_file(recognited_image, mimetype="image.jpeg", as_attachment=False)
