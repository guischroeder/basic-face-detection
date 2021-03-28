import requests

from moto import mock_s3
from app.main.libs.aws.aws_client import AWSClient
from app.main.libs.aws.s3_service import S3Service


class TestS3Service:
    @classmethod
    def setup_class(cls):
        cls._bucket_name = "test_bucket"
        cls._image_path = "test_image_path"
        cls._image_url = "http://test-image.com/image.jpeg"

    def setup_method(self):
        with mock_s3():
            self._client = AWSClient(
                "s3",
                {
                    "aws_access_key_id": "test_key",
                    "aws_secret_access_key": "test_secret",
                },
            )

        self._service = S3Service(self._client)

    @mock_s3
    def test_upload_image_from_url(self, mocker):
        s3 = self._client.get_instance()
        s3.create_bucket(Bucket=self._bucket_name)

        mocker.spy(s3, "put_object")
        mocker.patch("requests.get", return_value=mocker.Mock(content=self._image_url))

        self._service.upload_image_from_url(
            image_url=self._image_url,
            bucket_name=self._bucket_name,
            image_path=self._image_path,
        )

        s3.put_object.assert_called_once_with(
            Bucket=self._bucket_name, Key=self._image_path, Body=self._image_url
        )

    @mock_s3
    def test_get_image(self, mocker):
        s3 = self._client.get_instance()
        s3.create_bucket(Bucket=self._bucket_name)
        s3.put_object(
            Bucket=self._bucket_name,
            Key=self._image_path,
            Body=bytes(self._image_url, encoding="UTF-8"),
        )

        mocker.spy(s3, "get_object")

        self._service.get_image(
            bucket_name=self._bucket_name, image_path=self._image_path
        )

        s3.get_object.assert_called_once_with(
            Bucket=self._bucket_name, Key=self._image_path,
        )
