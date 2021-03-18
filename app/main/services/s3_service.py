import requests


class S3Service:
    def __init__(self, aws_client):
        self._aws_client = aws_client

    def upload_image_from_url(self, image_url, bucket, key):
        response = requests.get(image_url)

        return self._put_object(
            {"Bucket": bucket, "Key": key, "Body": response.content}
        )

    def _put_object(self, params):
        return self._aws_client.get_instance().put_object(**params)
