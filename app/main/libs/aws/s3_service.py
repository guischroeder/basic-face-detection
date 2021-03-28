import requests


class S3Service:
    def __init__(self, s3_client):
        self._s3_client = s3_client

    def upload_image_from_url(self, image_url, bucket_name, image_path):
        response = requests.get(image_url)

        return self._put_object(
            {"Bucket": bucket_name, "Key": image_path, "Body": response.content}
        )

    def get_image(self, bucket_name, image_path):
        return self._get_object(bucket_name, image_path)

    def _put_object(self, params):
        return self._s3_client.get_instance().put_object(**params)

    def _get_object(self, bucket_name, image_path):
        return self._s3_client.get_instance().get_object(
            Bucket=bucket_name, Key=image_path
        )
