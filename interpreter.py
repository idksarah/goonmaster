import keyboard
import time
from translate import MorseCodeTranslator
from imageSearch import ImageSearch
from openImage import OpenImage
    
translator = MorseCodeTranslator()
search = ImageSearch()
openImage = OpenImage()

# OpenImage.openImage('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRngGF6K9KVSyUaa3wRET32_OHo47WJgmcug17bw5Z8CeW-7p7MhBHcCigfRAw&s')

input = ''

prev = False
current = False
gap = 0

DEBOUNCE_TIME = .1
SPACE_TIME = .5

def addSpace():
    global input
    global gap
    if gap > SPACE_TIME and len(input) > 0 and not (input[-1] == ' '):
        input += ' '
        gap = 0

def imageSearch(p_text):
    return search.getImageUrl(p_text)

while True:
    addSpace()

    if keyboard.is_pressed('space'):
        print
        gap = 0
        current = True
    else:
        current = False
        gap += DEBOUNCE_TIME
    
    if prev and not current:
        input = input + '.'
        print(input)
    elif prev == current and current == True:
        input = input + '-'
        current = False
        print(input)

    if keyboard.is_pressed('enter'):
        translated = translator.translate_morse(input)
        print(translated)
        image_url = imageSearch(translated)
        print(image_url)
        OpenImage.openImage(image_url)
        input = ''

    if keyboard.is_pressed('backspace'):
        if (len(input) > 0):
            input = input[:-1]
        if (len(input) > 0 and input[-1] == ' '):
            input = input[:-1]
        
        print(input)

    prev = current
    time.sleep(DEBOUNCE_TIME) 
