import random
from math import *


configFile = open("config.txt")
configText = configFile.read()
configFile.close()

class Person:
    num = 0
    radius = 5
<<<<<<< HEAD
    exec(configText)
    
=======
    colors = ["deepskyblue2","red3", "grey70"]
>>>>>>> 77a8aae327ad1819cdb3addf70c86572f6263ee9
    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = Person.colors[0]
        self.dot = can.create_oval(self.x-Person.radius, self.y-Person.radius, self.x+Person.radius, self.y+Person.radius, fill=self.color)
        self.lastMove = [0,random.random()*360]
        self.health = 0 #0 is healthy, 1 is infected, 2 is clear, and 3 is dead
        self.recoveryTime = 0
        Person.num += 1

    def colorChange(self, can, Grp=1):
        self.color = Person.colors[Grp]
        can.itemconfig(self.dot, fill=self.color)
        self.health = Grp

    def distanceBetween(self, other):
        xDiff = abs(self.x-other.x)
        yDiff = abs(self.y-other.y)
        distBtwn = sqrt(xDiff**2 + yDiff**2)
        print(distBtwn)
        return distBtwn

    def moveUpdate(self,coords):
        self.x = coords[0]
        self.y = coords[1]
