from pyautogui import *
import pyautogui
import time
from multiprocessing import Process
import keyboard

timesLost = 1
tie = bool
win = bool
side = True


def punto():
    if timesLost == 0:
        click(585, 570)
    elif timesLost == 1:
        for i in range(3):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 2:
        for i in range(6):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 3:
        for i in range(12):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 4:
        for i in range(24):
            click(585, 570)
            time.sleep(0.3)
    elif timesLost == 5:
        for i in range(48):
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
        for i in range(3):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 2:
        for i in range(6):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 3:
        for i in range(12):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 4:
        for i in range(24):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 5:
        for i in range(48):
            click(1230, 570)
            time.sleep(0.3)
    elif timesLost == 6:
        for i in range(64):
            click(1230, 570)
            time.sleep(0.3)


def bet():
    click(1600, 800)


# Game starts

def empate():
    global tie
    if pyautogui.locateOnScreen('tie.png', region=(770, 810, 300, 100), confidence=0.7):
        tie = True
        print('empate')
        time.sleep(0.1)


def game():
    while not keyboard.is_pressed('x'):

        # Global variables
        global tie
        global timesLost
        global win
        global side

        # Limit check
        if timesLost == 5:
            timesLost = 1

        # Checks
        if pyautogui.locateOnScreen('screen.png', region=(1170, 835, 50, 50)):
            print('sin premio')
            win = False
            # time.sleep(1)
        else:
            print('hay fichas, hay ganancia')
            win = True
            # time.sleep(1)

        # Sets
        if not win:
            print('SE SUMA')
            timesLost += 1
        elif win and tie:
            print('SE CONTINUA')
        elif win:
            print('SE RESETEA')
            timesLost = 1

        tie = False

        # Bets

        print(timesLost)

        if side:
            print('Punto')
            punto()
            side = False
        elif not side:
            print('Banca')
            banca()
            side = True

        time.sleep(0.5)
        bet()
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
