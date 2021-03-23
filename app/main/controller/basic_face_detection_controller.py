from flask import Blueprint
from app.main.libs.hackattic.hackattic_service import HackatticService
from app.main.libs.aws.aws_client import AWSClient
from app.main.libs.aws.s3_service import S3Service
from app.main.libs.aws.rekognition_service import RekognitionService
from app.main.libs.face_detection.positions_service import PositionsService
from app.main.libs.challenge_solver import ChallengeSolver
from app.main.handle_error import handle_error
from app.main.config import config


basic_face_detection_bp = Blueprint("basic_face_detection", __name__)


@basic_face_detection_bp.app_errorhandler(Exception)
def error_handler(e):
    return handle_error(e)


@basic_face_detection_bp.route("/solve", methods=["GET"])
def get():
    s3_client = AWSClient(aws_service="s3", config=config["s3"])
    rekognition_client = AWSClient(
        aws_service="rekognition", config=config["rekognition"]
    )

    hackattic_service = HackatticService(config["hackattic"])
    s3_service = S3Service(s3_client)
    rekognition_service = RekognitionService(rekognition_client)
    position_service = PositionsService()

    challenge_solver = ChallengeSolver(
        hackattic_service=hackattic_service,
        s3_service=s3_service,
        rekognition_service=rekognition_service,
        position_service=position_service,
    )

    return challenge_solver.solve_the_problem()
