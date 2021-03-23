import io

from PIL import Image, ImageDraw
from app.main.general import BUCKET_NAME, IMAGE_PATH, FINAL_IMAGE_PATH


class ImageService:
    def __init__(self, position_service, s3_service):
        self._position_service = position_service
        self._s3_service = s3_service

    def generate_recognited_image(self, detected_faces_response):
        s3_response = self._s3_service.get_image(BUCKET_NAME, IMAGE_PATH)

        if not s3_response["Body"]:
            raise Exception("Can't generate the recognited image")

        stream = io.BytesIO(s3_response["Body"].read())
        image = Image.open(stream)
        draw = ImageDraw.Draw(image)

        for bounding_box in self._position_service.get_bounding_boxes_positions(
            detected_faces_response
        ):
            x = bounding_box["x"]
            y = bounding_box["y"]
            width = bounding_box["width"]
            height = bounding_box["height"]

            points = (
                (x, y),
                (x + width, y),
                (x + width, y + height),
                (x, y + height),
                (x, y),
            )

            draw.line(points, fill="#00d400", width=2)

        buffer = io.BytesIO()
        image.save(buffer, format="jpeg")

        return io.BytesIO(buffer.getvalue())
