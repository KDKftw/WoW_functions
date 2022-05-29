import pyautogui as p
import time
x=0
while True:
    p.press("space")
    time.sleep(10)
    x=x+1
    print(x)

    p.click()

    if x ==10:
        p.press("shift")
        x=0

    else:
        pass