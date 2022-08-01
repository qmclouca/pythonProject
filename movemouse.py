import random
import time

import pyautogui

x = pyautogui.size().width/2
y = pyautogui.size().height/2
pyautogui.moveTo(x, y)

try:
    while True:
        time.sleep(1)
        pyautogui.moveTo(x-2, y-2)
        time.sleep(1)
        pyautogui.moveTo(x + 2, y + 2)
except KeyboardInterrupt:
    print('finalization!')
