import json
import requests


class HackatticClient:
    _base_url = "https://hackattic.com/challenges/basic_face_detection/{section}"

    def __init__(self, config):
        self._access_token_qs = "?access_token=" + config["access_token"]

    def get_problem(self):
        url = self._base_url.replace("{section}", "problem") + self._access_token_qs

        return requests.get(url).json()

    def solve(self, positions):
        url = (
            self._base_url.replace("{section}", "solve") + self._access_token_qs
        )

        body = json.dumps({
            "face_tiles": positions
        })

        return requests.post(url, body).json()
