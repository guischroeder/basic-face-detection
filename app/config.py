import os

from dotenv import load_dotenv


load_dotenv()

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
