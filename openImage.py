from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np

class OpenImage:
    @staticmethod
    def openImage(image_url):
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch image: {e}")
            return

        if "image" not in response.headers.get("Content-Type", ""):
            print("URL did not return an image.")
            return

        try:
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            img_np = np.array(img)

            if img_np.ndim == 3:
                img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            cv2.imshow('Image', img_np)
            cv2.setWindowProperty("Image", cv2.WND_PROP_TOPMOST, 1)

            print("Press space or ESC to close the image window.")

            while True:
                key = cv2.waitKey(10)
                if key == ord(' ') or key == 27:
                    break

            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error opening image: {e}")
