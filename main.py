import keyboard
import time
from translate import MorseCodeTranslator
from imageSearch import ImageSearch
    
translator = MorseCodeTranslator()
search = ImageSearch()

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
    print("FUCKING TEXT" + p_text)
    print(search.getImageUrl(p_text))

print("IM GONNA FUCKING goon")

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
        imageSearch(translator.translate_morse(input))
        input = ''

    if keyboard.is_pressed('backspace'):
        if (len(input) > 0):
            input = input[:-1]
        if (len(input) > 0 and input[-1] == ' '):
            input = input[:-1]
        
        print(input)

    prev = current
    time.sleep(DEBOUNCE_TIME) 
