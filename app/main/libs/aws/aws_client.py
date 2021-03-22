import boto3


class AWSClient:
    _client = None

    def __init__(self, aws_service, region_name, credentials):
        self._aws_service = aws_service
        self._region_name = region_name
        self._credentials = credentials

    def get_instance(self):
        if not self._client:
            self._client = boto3.client(
                self._aws_service, region_name=self._region_name, **self._credentials
            )

        return self._client
