import pyautogui as p
import time

def jenKlikej():
    while True:
        time.sleep(2)
        p.click()
        time.sleep(180)

jenKlikej()

def jenKlikejRight():
    while True:
        p.click(button='right')
        time.sleep(0.15)

##jenKlikejRight()
test = 5+1+3+1+13+11+12+5
def soemthinggg():
    print(test)
    while True:
        time.sleep(6)
        p.click(button='right')
        p.moveTo(1135, 456)
        time.sleep(15)
        p.click(button='right')
        p.moveTo(879, 455)



