from Scene import *
import random
import time


newScene = Scene(pplCount=250,socialDist=1)
newScene.movement()
while True:
    if newScene.moving == 1:
        newScene.movement()
    newScene.master.after(100)
    newScene.master.update()
