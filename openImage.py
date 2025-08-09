from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np
import keyboard

class OpenImage:
    @staticmethod
    def openImage(image_url):
        response = requests.get(image_url)
        response.raise_for_status()

        image_data = BytesIO(response.content)

        img = Image.open(image_data)

        img_np = np.array(img)

        if img_np.ndim == 3:
            img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        cv2.imshow('Image', img_np)
        # cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, 1)
        cv2.setWindowProperty("Image", cv2.WND_PROP_TOPMOST, 1)

        while True:
            if keyboard.is_pressed('space'):
                break
            if cv2.waitKey(10) & 0xFF == 27:
                break

        cv2.destroyAllWindows()
