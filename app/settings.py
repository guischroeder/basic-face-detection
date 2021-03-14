import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    @staticmethod
    def hackattic_credentials():
        return {"access_token": os.getenv("HACKATTIC_ACCESS_TOKEN")}

    @staticmethod
    def aws_s3_credentials():
        return {
            "access_key": os.getenv("S3_ACCESS_KEY"),
            "secret_access_key": os.getenv("S3_SECRET_ACCESS_KEY"),
        }

    @staticmethod
    def aws_rekognition_credentials():
        return {
            "access_key": os.getenv("REKOGNITION_ACCESS_KEY"),
            "secret_access_key": os.getenv("REKOGNITION_SECRET_ACCESS_KEY"),
        }
