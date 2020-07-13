import pyautogui as gui
from time import sleep
from os import system

counter = 0

def fGetRGB(x,y):
    return gui.screenshot().getpixel((x,y))

def fCheckColor(temp_list):
    
    key = False
    color = ((134,148,182),(154,168,202)) #a color between red and blue

    if (temp_list[0] >= color[0][0] and temp_list[0] <= color[1][0]):
        key = True
    
    return key

def fClick(x,y):
    while True:
        if gui.position() == (x,y):
            gui.click()
            break
        else:
            gui.moveTo(x,y)


sleep(2)    #first delay. delay for starting the bot and alt + tab the game

while True:
    system("cls")
    print("number of fish caught: " + str(counter))
    fClick(554,784) #fishing hole position on the screen
    while True:
        if (fCheckColor(fGetRGB(513,814))):
            fClick(509,773) #pull button position on the screen
            counter += 1
            break
        else:
            continue
    sleep(5)
    fClick(512,741) #ok button (after fishing character looks and defines the fish we wait for that and click ok button)
    sleep(1)