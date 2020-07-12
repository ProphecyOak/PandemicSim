import random
from math import *


configFile = open("config.txt")
configText = configFile.readlines()
configFile.close()

class Person:
    num = 0
    exec(configText[0])
    exec(configText[1])

    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = Person.colors[0]
        self.lightColor = Person.lightColors[0]
        self.dot = can.create_oval(self.x-Person.radius, self.y-Person.radius, self.x+Person.radius, self.y+Person.radius, fill=self.color)
        self.outerCircle = can.create_oval(self.x-Person.radius*6, self.y-Person.radius*6, self.x+Person.radius*6, self.y+Person.radius*6, fill = self.lightColor)
        self.lastMove = [0,random.random()*360]
        self.health = 0 #0 is healthy, 1 is infected, 2 is clear, and 3 is dead
        self.recoveryTime = 0
        Person.num += 1

    def colorChange(self, can, Grp=1):
        self.color = Person.colors[Grp]
        self.lightColor = Person.lightColors[Grp]
        can.itemconfig(self.dot, fill=self.color)
        can.itemconfig(self.outerCircle, fill=self.lightColor)
        self.health = Grp

    def distanceBetween(self, other):
        xDiff = abs(self.x-other.x)
        yDiff = abs(self.y-other.y)
        distBtwn = sqrt(xDiff**2 + yDiff**2)
        return distBtwn

    def moveUpdate(self,coords):
        self.x = coords[0]
        self.y = coords[1]
