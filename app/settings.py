import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    @staticmethod
    def hackattic_access_token():
        return os.getenv("HACKATTIC_ACCESS_TOKEN")

    @staticmethod
    def s3_credentials():
        return {
            "aws_access_key_id": os.getenv("S3_ACCESS_KEY"),
            "aws_secret_access_key": os.getenv("S3_SECRET_ACCESS_KEY"),
        }

    @staticmethod
    def s3_bucket_name():
        return os.getenv("S3_BUCKET")

    @staticmethod
    def rekognition_credentials():
        return {
            "aws_access_key_id": os.getenv("REKOGNITION_ACCESS_KEY"),
            "aws_secret_access_key": os.getenv("REKOGNITION_SECRET_ACCESS_KEY"),
        }
