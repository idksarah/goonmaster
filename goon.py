import keyboard
import time

input = ''

prev = False
current = False
gap = 0

DEBOUNCE_TIME = .1
SPACE_TIME = .5

def addSpace():
    global input
    global gap
    # print(gap)
    if gap > SPACE_TIME and len(input) > 0 and not (input[-1] == ' '):
        input += ' '
        gap = 0

while True:
    addSpace() # fix ts

    if keyboard.is_pressed('space'):
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

    prev = current
    time.sleep(DEBOUNCE_TIME) 