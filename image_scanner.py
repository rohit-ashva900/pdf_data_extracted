from google.cloud import vision
import io
from PIL import Image


def extract_text_from_image(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    text = response.full_text_annotation.text

    return text
