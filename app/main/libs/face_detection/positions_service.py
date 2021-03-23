from app.main.helpers.position_helper import find_position, center_of_square
from app.main.general import IMAGE_HEIGHT, IMAGE_WIDTH


class PositionsService:
    def findPositions(self, detect_faces):
        boundingBoxesPositions = self._getBoundingBoxesPositions(detect_faces)

        positions = [
            [
                find_position(center_of_square(boundingBox["x"], boundingBox["width"])),
                find_position(
                    center_of_square(boundingBox["y"], boundingBox["height"])
                ),
            ]
            for boundingBox in boundingBoxesPositions
        ]

        return positions

    def _getBoundingBoxesPositions(self, detected_faces):
        if not detected_faces or not detected_faces["FaceDetails"]:
            raise Exception("Can't get bounding boxes positions.")

        return [
            {
                "x": detected_face["BoundingBox"]["Left"] * IMAGE_WIDTH,
                "y": detected_face["BoundingBox"]["Top"] * IMAGE_HEIGHT,
                "width": detected_face["BoundingBox"]["Width"] * IMAGE_WIDTH,
                "height": detected_face["BoundingBox"]["Height"] * IMAGE_HEIGHT,
            }
            for detected_face in detected_faces["FaceDetails"]
        ]
