from displayData import *
import random
import time

newScene = Scene(pplCount=100)
while True:
    if newScene.moving == 1:
        newScene.movement()
    newScene.master.after(100)
    newScene.master.update()
