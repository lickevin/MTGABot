import time

from src.actionController import *

try:
    while True:
        time.sleep(0.5)
        goBack()
except KeyboardInterrupt:
    pass