from app.utils.constants import BUCKET_NAME, IMAGE_PATH


class FaceDetectionFacade:
    def __init__(
        self,
        hackattic_service,
        s3_service,
        rekognition_service,
        positions_service,
        image_service,
    ):
        self._hackattic_service = hackattic_service
        self._s3_service = s3_service
        self._rekognition_service = rekognition_service
        self._positions_service = positions_service
        self._image_service = image_service

    def show_detected_faces(self):
        faces = self._detect_faces()

        positions = self._positions_service.find_positions(faces)

        return self._image_service.generate_recognited_image(faces)

    def solve_problem(self):
        faces = self._detect_faces()

        positions = self._positions_service.find_positions(faces)

        self._hackattic_service.send_result(positions)

    def _detect_faces(self):
        image_url = self._hackattic_service.get_image_url()

        self._s3_service.upload_image_from_url(
            image_url=image_url, bucket_name=BUCKET_NAME, image_path=IMAGE_PATH,
        )

        return self._rekognition_service.detect_faces(
            bucket_name=BUCKET_NAME, image_path=IMAGE_PATH
        )
