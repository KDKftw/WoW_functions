import pyautogui as p
import time



def vyprazdniRadek(radekCislo):
###posun o x 46 +-

    posunX = 46
    defaultX = 1542
    for _ in range(8):

        p.moveTo(defaultX, radekCislo)
        #time.sleep(1)
        time.sleep(4)
        p.moveTo(defaultX, radekCislo)
        time.sleep(1)
        p.keyDown('alt')
        time.sleep(1)
        p.click(defaultX, radekCislo, button="right")
        defaultX = defaultX + posunX
        print(defaultX)
        time.sleep(5)  ##at this point item in auction, waiting to scan, avg looks like 3-4secs max
        p.moveTo(152, 442)
        time.sleep(1)
        p.click(152, 442)

##vyprazdniRadek(350)

def allInOne():
    radek2=350
    for _ in range(11):
        time.sleep(1)

        vyprazdniRadek(radek2)
        radek2 = radek2 + 43
        time.sleep(1)

allInOne()