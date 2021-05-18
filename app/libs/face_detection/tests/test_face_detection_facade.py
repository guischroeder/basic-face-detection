import requests

from io import BytesIO

from app.libs.hackattic.hackattic_service import HackatticService
from app.libs.aws.aws_client import AWSClient
from app.libs.aws.s3_service import S3Service
from app.libs.aws.rekognition_service import RekognitionService
from app.libs.face_detection.positions_service import PositionsService
from app.libs.face_detection.image_service import ImageService
from app.libs.face_detection.face_detection_facade import FaceDetectionFacade
from app.helpers.tests_helper import create_test_image


def build_facade(s3, rekognition):
    hackattic_service = HackatticService({"access_token": ""})
    s3_service = S3Service(s3)
    rekognition_service = RekognitionService(rekognition)
    positions_service = PositionsService()
    image_service = ImageService(positions_service, s3_service)

    return FaceDetectionFacade(
        hackattic_service=hackattic_service,
        s3_service=s3_service,
        rekognition_service=rekognition_service,
        positions_service=positions_service,
        image_service=image_service,
    )


def mock_s3(mocker, image):
    return mocker.Mock(
        put_object=lambda Bucket, Key, Body: {},
        get_object=lambda Bucket, Key: {"Body": image},
    )


def mock_rekognition(mocker, data):
    return mocker.Mock(detect_faces=lambda Image: data)


def mock_requests_get(mocker):
    mocker.patch(
        "requests.get", return_value=mocker.Mock(json=lambda: {"image_url": ""},),
    )


def test_show_detect_faces(mocker, data):
    mock_requests_get(mocker)
    image = create_test_image()
    s3_client = mocker.Mock(get_instance=lambda: mock_s3(mocker, image))
    rekognition_client = mocker.Mock(
        get_instance=lambda: mock_rekognition(mocker, data)
    )
    face_detection_facade = build_facade(s3_client, rekognition_client)

    get_image_url = mocker.spy(
        face_detection_facade._hackattic_service, "get_image_url"
    )
    upload_image_from_url = mocker.spy(
        face_detection_facade._s3_service, "upload_image_from_url"
    )
    detect_faces = mocker.spy(
        face_detection_facade._rekognition_service, "detect_faces"
    )
    find_positions = mocker.spy(
        face_detection_facade._positions_service, "find_positions"
    )

    final_image = face_detection_facade.show_detected_faces()

    assert isinstance(final_image, BytesIO)
    assert final_image != image
    assert find_positions.spy_return == [[2, 3], [0, 6], [4, 7]]
    get_image_url.assert_called_once()
    upload_image_from_url.assert_called_once()
    detect_faces.assert_called_once()


def test_solve_problem(mocker, data):
    mock_requests_get(mocker)
    s3_client = mocker.Mock(get_instance=lambda: mock_s3(mocker, {}))
    rekognition_client = mocker.Mock(
        get_instance=lambda: mock_rekognition(mocker, data)
    )
    face_detection_facade = build_facade(s3_client, rekognition_client)

    send_result = mocker.spy(face_detection_facade._hackattic_service, "send_result")

    face_detection_facade.solve_problem()

    send_result.assert_called_once_with([[2, 3], [0, 6], [4, 7]])
