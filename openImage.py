from PIL import Image
import requests
from io import BytesIO
import psutil
import keyboard
import cv2

class OpenImage:
    @staticmethod
    def openImage(image_url):
        response = requests.get(image_url)
        response.raise_for_status()

        image_data = BytesIO(response.content)

        img = Image.open(image_data)

        img.show()

        # cv2.imshow('img', img)
        # cv2.waitKey()
        # cv2.destroyAllWindows()