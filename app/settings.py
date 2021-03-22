import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    ### HACKATTIC ###
    @staticmethod
    def hackattic_access_token():
        return os.getenv("HACKATTIC_ACCESS_TOKEN")

    ### S3 ###
    @staticmethod
    def s3_credentials():
        return {
            "aws_access_key_id": os.getenv("S3_ACCESS_KEY"),
            "aws_secret_access_key": os.getenv("S3_SECRET_ACCESS_KEY"),
        }

    @staticmethod
    def s3_bucket():
        return {
            "name": os.getenv("S3_BUCKET"),
            "key": os.getenv("S3_BUCKET_IMAGE_PATH"),
            "region": os.getenv("S3_BUCKET_REGION"),
        }

    ### REKOGNITION ###
    @staticmethod
    def rekognition_credentials():
        return {
            "aws_access_key_id": os.getenv("REKOGNITION_ACCESS_KEY"),
            "aws_secret_access_key": os.getenv("REKOGNITION_SECRET_ACCESS_KEY"),
        }

    @staticmethod
    def rekognition_service_region():
        return os.getenv("REKOGNITION_SERVICE_REGION")
