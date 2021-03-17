import boto3
import requests


class S3Service:
    _s3_client = None

    def __init__(self, credentials):
        self._credentials = credentials

    def upload_image_from_url(self, image_url, bucket, key):
        response = requests.get(image_url)

        return self._put_object(
            {"Bucket": bucket, "Key": key, "Body": response.content}
        )

    def _put_object(self, params):
        return self._get_instance().put_object(**params)

    def _get_instance(self):
        if not self._s3_client:
            self._s3_client = boto3.client(
                "s3", region_name="us-west-1", **self._credentials
            )

        return self._s3_client
