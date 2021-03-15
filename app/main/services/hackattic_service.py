import requests


class HackatticService:
    _base_url = "https://hackattic.com/challenges/basic_face_detection/{section}"

    def __init__(self, credentials):
        self._credentials = credentials

    def get_image_url(self):
        url = self._base_url.replace("{section}", "problem")
        params = {"access_token": self._credentials.get("access_token")}

        response = requests.get(url, params).json()

        return response.get("image_url", "")
