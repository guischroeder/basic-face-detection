import requests


class HackatticClient:
    _base_url = "https://hackattic.com/challenges/basic_face_detection/{section}"

    def __init__(self, config):
        self._config = config

    def get_problem(self):
        url = self._base_url.replace("{section}", "problem")
        params = {"access_token": self._config["access_token"]}

        response = requests.get(url, params).json()

        return response
