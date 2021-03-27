import boto3

from app.main.libs.aws.aws_client import AWSClient


class TestAwsClient:
    def test_aws_client(self, mocker):
        @classmethod
        def setup_class(cls):
            cls._config = cls._config = {
                "aws_access_key_id": "test_key",
                "aws_secret_access_key": "test_secret",
                "region_name": "us-east-2",
            }

        def test_aws_client(self):
            client = AWSClient(aws_service="s3", config=self._config)

            mocker.spy(boto3, "client")

            assert client.get_instance() == client.get_instance()
            boto3.client.assert_called_once("s3", self._config)
