import requests

from app.libs.hackattic.hackattic_service import HackatticService


class TestHackatticService:
    @classmethod
    def setup_class(cls):
        cls._access_token = "test_token"

    def setup_method(self):
        self._hackattic_service = HackatticService({"access_token": self._access_token})

    def test_get_image_url(self, mocker):
        test_image = "http://test_image.com"

        mocker.patch(
            "requests.get",
            return_value=mocker.Mock(json=lambda: {"image_url": test_image},),
        )

        assert self._hackattic_service.get_image_url() == test_image
        requests.get.assert_called_once_with(
            f"https://hackattic.com/challenges/basic_face_detection/problem?access_token={self._access_token}"
        )

    def test_send_result(self, mocker):
        data = [[1, 2], [3, 4], [2, 1], [4, 3]]

        mocker.patch(
            "requests.post", return_value=mocker.Mock(json=lambda: {"result": True},)
        )

        assert self._hackattic_service.send_result(data) == {"result": True}
        requests.post.assert_called_once_with(
            f"https://hackattic.com/challenges/basic_face_detection/solve?access_token={self._access_token}",
            {"face_tiles": data},
        )
