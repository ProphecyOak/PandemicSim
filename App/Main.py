from Scene import *
import random
import time

<<<<<<< HEAD
newScene = Scene(pplCount=100)
=======

newScene = Scene(pplCount=20)

>>>>>>> 21aeaa7c70eed287d58f493d7b71de04380ca8fa
while True:
    if newScene.moving == 1:
        newScene.movement()
    newScene.master.after(100)
    newScene.master.update()
