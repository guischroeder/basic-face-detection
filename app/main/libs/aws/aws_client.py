import boto3


class AWSClient:
    _client = None

    def __init__(self, aws_service, config):
        self._aws_service = aws_service
        self._config = config

    def get_instance(self):
        if not self._client:
            self._client = boto3.client(self._aws_service, **self._config)

        return self._client
