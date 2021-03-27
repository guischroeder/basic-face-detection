import requests


class HackatticService:
    _base_url = "https://hackattic.com/challenges/basic_face_detection/{section}"

    def __init__(self, config):
        self._access_token_qs = "?access_token=" + config["access_token"]

    def get_image_url(self):
        url = self._base_url.replace("{section}", "problem") + self._access_token_qs

        response = requests.get(url).json()

        return response["image_url"]

    def solve(self, data):
        url = self._base_url.replace("{section}", "solve") + self._access_token_qs

        body = {"face_tiles": data}

        return requests.post(url, body).json()
