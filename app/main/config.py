import os

from dotenv import load_dotenv


load_dotenv()

config = {
    "hackattic": {"access_token": os.getenv("HACKATTIC_ACCESS_TOKEN"),},
    "s3": {
        "aws_access_key_id": os.getenv("S3_ACCESS_KEY"),
        "aws_secret_access_key": os.getenv("S3_SECRET_ACCESS_KEY"),
        "region_name": "us-west-1",
    },
    "rekognition": {
        "aws_access_key_id": os.getenv("REKOGNITION_ACCESS_KEY"),
        "aws_secret_access_key": os.getenv("REKOGNITION_SECRET_ACCESS_KEY"),
        "region_name": "us-west-1",
    },
}
