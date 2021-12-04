import pyautogui as p
import time
##nastaveno na bagly huntera tak s tim nemanipulovat no
import keyboard
radek = ["l", "l", "l", "l", "l", "L", "l", "s"]

def vyprazdniRadek(radekCislo):
###posun o x 46 +-
    radek1= 350
    posunX = 46
    defaultX = 1586
    for x in radek:

        p.moveTo(defaultX, radekCislo)
        time.sleep(1)
        p.click(defaultX, radekCislo, button='right')
        defaultX = defaultX + posunX
        print(defaultX)


##vyprazdniRadek()

##43 dolů
def allInOne():
    radek2 = 350



    for x in radek:
        time.sleep(0.5)
        vyprazdniRadek(radek2)
        radek2 = radek2 + 43
        time.sleep(1)
    #if keyboard.is_pressed('c'):
     #   break

allInOne()
