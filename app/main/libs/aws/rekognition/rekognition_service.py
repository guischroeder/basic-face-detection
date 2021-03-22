class RekognitionService:
    def __init__(self, rekognition_client):
        self._rekognition_client = rekognition_client

    def detect_faces(self, bucket_name, key):
        return self._rekognition_client.get_instance().detect_faces(
            Image={"S3Object": {"Bucket": bucket_name, "Name": key,}},
        )
