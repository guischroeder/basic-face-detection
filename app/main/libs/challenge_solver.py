from app.main.general import BUCKET_NAME, IMAGE_PATH


class ChallengeSolver:
    def __init__(
        self, hackattic_service, s3_service, rekognition_service, position_service
    ):
        self._hackattic_service = hackattic_service
        self._s3_service = s3_service
        self._rekognition_service = rekognition_service
        self._position_service = position_service

    def solve_the_problem(self):
        faces = self._detect_faces()

        positions = self._position_service.find_positions(faces)

        return self._hackattic_service.solve(positions)

    def _detect_faces(self):
        image_url = self._hackattic_service.get_problem().get("image_url", "")

        self._s3_service.upload_image_from_url(
            image_url=image_url, bucket_name=BUCKET_NAME, image_path=IMAGE_PATH,
        )

        return self._rekognition_service.detect_faces(
            bucket_name=BUCKET_NAME, image_path=IMAGE_PATH
        )
