from pyautogui import *
import pyautogui
import time
from multiprocessing import Process
import keyboard
import sys
import numpy as np

timesLost = 0
tie = bool
win = bool
side = bool
cards = False

def exit():
    if keyboard.is_pressed('x'):
        sys.exit()

def punto():
    if timesLost == 0:
        click(585, 570)
    elif timesLost == 1:
        for i in range(2):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 2:
        for i in range(4):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 3:
        for i in range(8):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 4:
        for i in range(16):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 5:
        for i in range(32):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 6:
        for i in range(64):
            click(585, 570)
            time.sleep(0.3)


def banca():
    if timesLost == 0:
        click(1230, 570)
    elif timesLost == 1:
        for i in range(2):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 2:
        for i in range(4):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 3:
        for i in range(8):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 4:
        for i in range(16):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 5:
        for i in range(32):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 6:
        for i in range(64):
            click(1230, 570)
            time.sleep(0.3)


def bet():
    click(1600, 800)

def random1():
    global side
    side = True
    print('RANDOM-L')

def random2():
    global side
    side = False
    print('RANDOM-R')

def random():

    rad = np.random.randint(2)

    if rad == 0:
        random1()
    elif rad == 1:
        random2()

def chooseSide():

    global side
    if timesLost == 0:
        random()
    elif timesLost == 1:
        random()
    elif timesLost == 2:
        random()
    elif timesLost == 3:
        random()
    elif timesLost == 4:
        random()
    elif timesLost == 5:
        random()
    else:
        random()

# Game starts

def empate():
    global tie
    if pyautogui.locateOnScreen('tie.png', region=(770, 810, 300, 100), confidence=0.7):
        tie = True
        print('empate')
        time.sleep(0.1)

def waitTill():
    global cards
    while True:
        while not cards:

            if pyautogui.locateOnScreen('playball.png', region=(470, 250, 900, 250), confidence=0.9):
                print('NO HAY CARTAS')
                cards = False
                time.sleep(1)
            else:
                print('Play Time')
                cards = True
        if cards:
            cards = False
            break

def game():
    while True:

        exit()
        # Global variables
        global tie
        global timesLost
        global win
        global side
        global cards


        # Limit check
        if timesLost == 5:
            timesLost = 0

        # Checks
        if pyautogui.locateOnScreen('screen.png', region=(1170, 835, 50, 50)):
            print('sin premio')
            win = False
        else:
            print('hay fichas, hay ganancia')
            win = True

        exit()

        # Sets
        if not win:
            print('SE SUMA')
            timesLost += 1
        elif win and tie:
            print('SE CONTINUA')
        elif win:
            print('SE RESETEA')
            timesLost = 0

        tie = False

        exit()

        # Bets

        print(timesLost)

        chooseSide()

        if side:
            print('Punto')
            punto()
            side = False
        elif not side:
            print('Banca')
            banca()
            side = True

        time.sleep(0.5)
        exit()
        bet()

        # If cards are found... start counting
        waitTill()

        empate()
        time.sleep(1)
        empate()
        time.sleep(1)
        empate()
        time.sleep(1)
        empate()
        time.sleep(1)
        empate()
        time.sleep(1)




if __name__ == '__main__':
    p1 = Process(target=empate)
    p1.start()
    p2 = Process(target=game)
    p2.start()
    p1.join()
    p2.join()