# Basic Face Detection

This project solves the **Basic Face Detection** problem from [Hackattic](https://hackattic.com/challenges/basic_face_detection).

## Installation
Be sure you have [Poetry](https://python-poetry.org) installed.

- Fork or clone the project
- Execute `poetry install` inside the project folder
- To run the app execute `python3 run.py`

## Configuration
To run the project you need to create an account in [Hackattic](https://hackattic.com/register), [AWS](https://aws.amazon.com/) and [IAM](https://aws.amazon.com/iam/).

As soon as you have an account you gonna create users for [Amazon S3](https://aws.amazon.com/s3/?nc2=h_ql_prod_st_s3) and [Amazon Rekognition](https://aws.amazon.com/rekognition/?nc2=type_a). Also, create a bucket in S3.

In `config.py` you might change the `region_name` according to your region. Don't forget that the region chosen for the bucket and for the rekognition service must be the same.

Create a `.env` file in the root folder and set your credentials:
```
HACKATTIC_ACCESS_TOKEN=your_access_token

S3_ACCESS_KEY=your_access_key
S3_SECRET_ACCESS_KEY=your_secret_access_key

REKOGNITION_ACCESS_KEY=your_access_token
REKOGNITION_SECRET_ACCESS_KEY=your_secret_access_key
```

## Tests
[Pytest](https://docs.pytest.org/en/stable/) was used to test the code. Be sure you installed it as so as the other dev dependencies.

By doing this you are good to go executing `python -m pytest`.

## API
The endpoint `/basic-face-detection/solve` will show you the faces in the image provided by Hackattic. Running in your localhost it might take a while due to the AWS services latency. Also, sometimes, you may get a timeout error from Hackattic when trying to solve the challange. You can check your latency [here](https://ping.psa.fun/) and choose the region with the lowest ping to set in the config file. Another way to solve this is by running the app in a virtual machine with [ec2](https://aws.amazon.com/ec2/) so you can set to be in the same region of other required services.

![image](https://user-images.githubusercontent.com/53911589/112843869-739c5580-9079-11eb-8429-300fe816a397.png)
