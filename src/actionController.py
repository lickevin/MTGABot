import pyautogui as ag
import time

def passPriority():
    time.sleep(0.5)
    ag.keyDown('space')
    time.sleep(0.1)
    ag.keyUp('space')

def goBack():
    time.sleep(0.5)
    ag.keyDown('y')
    time.sleep(0.1)
    ag.keyUp('y')

# Functions copied from https://github.com/misprit7/MTGAI/blob/master/src/gamecontroller.py

def click():
    ag.mouseDown()
    time.sleep(0.1)
    ag.mouseUp()

# Have to scroll in chunks for arena to accept it
def scroll(amount):
    for i in range(amount if amount > 0 else -amount):
        ag.scroll(5 if amount > 0 else -5)


# Have to hold a bit for arena to accept it
def press(key):
    ag.keyDown(key)
    time.sleep(0.1)
    ag.keyUp(key)

# Consistent spot to reset mouse to
def mreset():
    ag.moveTo(50, 540)


def dragcard(pos):
    ag.moveTo(pos[0], pos[1], duration=0.1)
    ag.dragTo(960, 540, duration=0.3)