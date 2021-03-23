from app.main.helpers.position_helper import find_position, center_of_square
from app.main.constants import IMAGE_HEIGHT, IMAGE_WIDTH


class PositionsService:
    def find_positions(self, detected_faces_response):
        bounding_boxes_positions = self.get_bounding_boxes_positions(
            detected_faces_response
        )

        positions = [
            [
                find_position(
                    center_of_square(bounding_box["x"], bounding_box["width"])
                ),
                find_position(
                    center_of_square(bounding_box["y"], bounding_box["height"])
                ),
            ]
            for bounding_box in bounding_boxes_positions
        ]

        return positions

    def get_bounding_boxes_positions(self, detected_faces_response):
        if not detected_faces_response or not detected_faces_response["FaceDetails"]:
            raise Exception("Can't get bounding boxes positions.")

        return [
            {
                "x": detected_face["BoundingBox"]["Left"] * IMAGE_WIDTH,
                "y": detected_face["BoundingBox"]["Top"] * IMAGE_HEIGHT,
                "width": detected_face["BoundingBox"]["Width"] * IMAGE_WIDTH,
                "height": detected_face["BoundingBox"]["Height"] * IMAGE_HEIGHT,
            }
            for detected_face in detected_faces_response["FaceDetails"]
        ]
