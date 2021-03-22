import requests


class S3Service:
    def __init__(self, s3_client):
        self._s3_client = s3_client

    def upload_image_from_url(self, image_url, bucket_name, key):
        response = requests.get(image_url)

        return self._put_object(
            {"Bucket": bucket_name, "Key": key, "Body": response.content}
        )

    def _put_object(self, params):
        return self._s3_client.get_instance().put_object(**params)
