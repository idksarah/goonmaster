import keyboard
import time
from translate import MorseCodeTranslator
from imageSearch import ImageSearch
from openImage import OpenImage

class Interpreter:
    @staticmethod
    def interpret():
        translator = MorseCodeTranslator()
        search = ImageSearch()
        open_image = OpenImage()

        morse_input = ''
        prev = False
        current = False
        gap = 0

        DEBOUNCE_TIME = 0.1
        SPACE_TIME = 0.5

        def add_space():
            nonlocal morse_input, gap
            if gap > SPACE_TIME and len(morse_input) > 0 and not morse_input.endswith(' '):
                morse_input += ' '
                gap = 0

        def image_search(p_text):
            return search.getImageUrl(p_text)

        while True:
            add_space()

            if keyboard.is_pressed('space'):
                gap = 0
                current = True
            else:
                current = False
                gap += DEBOUNCE_TIME

            if prev and not current:
                morse_input += '.'
                print(morse_input)
            elif prev == current and current is True:
                morse_input += '-'
                current = False
                print(morse_input)

            if keyboard.is_pressed('enter'):
                translated = translator.translate_morse(morse_input)
                # print(translated)
                morse_input = ''
                image_url = image_search(translated)
                return image_url
                # print(image_url)
                # open_image.openImage(image_url)

            if keyboard.is_pressed('backspace'):
                if len(morse_input) > 0:
                    morse_input = morse_input[:-1]
                if len(morse_input) > 0 and morse_input.endswith(' '):
                    morse_input = morse_input[:-1]
                print(morse_input)

            prev = current
            time.sleep(DEBOUNCE_TIME)
