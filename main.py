import time
import random
import pyautogui

def movemouse():
    for z in range(1, 10):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        pyautogui.moveTo(x,y)
        time.sleep(2)

if __name__ == '__main__':
    movemouse()
