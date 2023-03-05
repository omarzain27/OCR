import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types



def Vision (need):
    content = need
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision.json'
    client = vision_v1.ImageAnnotatorClient()
    image = vision_v1.types.Image(content=content)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text
    return docText
