import pyautogui as p
import time


##mezera mezi prvnim item a druhym v radku 76,225   +53Y
##                                         76,278
                                        ##125
                                        ##14 sloupcu celkove
l = ["l", "l", "l", "l", "l", "L"]
pocet_sloupcu = ["l", "l", "l0", "l", "l", "l", "l", "l", "l", "l", "l" , "s", "l", "l"]

def radek(sloupec):

    posunY = 51
    lokaceY = 225
    p.moveTo(sloupec, lokaceY)
    time.sleep(1.5)
    p.click(sloupec, lokaceY, button='right')
    time.sleep(0.5)
    for x in l:
        p.moveTo(sloupec, lokaceY+posunY)
        time.sleep(1.5)
        p.click(sloupec, lokaceY+posunY, button='right')
        print("test")
        posunY= posunY + 47
        print(posunY)
        time.sleep(0.5)

def allInOne():
    sloupecLokace = 76
    for x in pocet_sloupcu:

        radek(sloupecLokace)
        sloupecLokace = sloupecLokace + 53
        time.sleep(2)




allInOne()