import io

from PIL import Image, ImageDraw
from app.main.constants import BUCKET_NAME, IMAGE_PATH, FINAL_IMAGE_PATH


class ImageService:
    _bucket_name = BUCKET_NAME
    _image_path = IMAGE_PATH

    def __init__(self, positions_service, s3_service):
        self._positions_services = positions_service
        self._s3_service = s3_service

    def generate_recognited_image(self, detected_faces_response):
        s3_response = self._s3_service.get_image(self._bucket_name, self._image_path)

        if not s3_response["Body"]:
            raise Exception("Can't generate the recognited image")

        buffer = io.BytesIO(s3_response["Body"].read())
        image = Image.open(buffer)

        bounding_boxes = self._positions_services.get_bounding_boxes_positions(
            detected_faces_response
        )
        final_image = self._highlight_faces(image, bounding_boxes)

        final_image_buffer = io.BytesIO()
        final_image.save(final_image_buffer, format="jpeg")

        return io.BytesIO(final_image_buffer.getvalue())

    def _highlight_faces(self, image, bounding_boxes):
        draw = ImageDraw.Draw(image)

        for bounding_box in bounding_boxes:
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

        return image
