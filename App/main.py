from displayData import *
import random
import time

newScene = Scene(pplCount=6)
while True:
    newScene.movement()
    newScene.master.after(1)
    newScene.master.update()
