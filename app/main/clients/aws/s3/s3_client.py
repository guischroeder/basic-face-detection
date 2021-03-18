import boto3
from app.main.clients.aws.aws_client import AWSClient


class S3Client(AWSClient):
    _client = None

    def __init__(self, credentials):
        self._credentials = credentials

    def get_instance(self):
        if not self._client:
            self._client = boto3.client("s3", **self._credentials)

        return self._client
