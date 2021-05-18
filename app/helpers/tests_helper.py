from io import BytesIO
from PIL import Image


def create_test_image():
    file = BytesIO()
    image = Image.new("RGB", (800, 800), color="white")
    image.save(file, "jpeg")
    file.name = "test.jpeg"
    file.seek(0)

    return file
