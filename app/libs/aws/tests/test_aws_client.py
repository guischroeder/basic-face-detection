import boto3

from app.libs.aws.aws_client import AWSClient


def test_aws_client(mocker):
    config = {
        "aws_access_key_id": "test_key",
        "aws_secret_access_key": "test_secret",
        "region_name": "us-east-2",
    }
    client = AWSClient("s3", config)

    mocker.spy(boto3, "client")

    assert client.get_instance() == client.get_instance()
    boto3.client.assert_called_once_with("s3", **config)
