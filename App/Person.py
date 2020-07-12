import random
from math import *


configFile = open("config.txt")
configText = configFile.read()
configFile.close()

class Person:
    num = 0
    radius = 5
    exec(configText)
    
    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = Person.colors[0]
        self.dot = can.create_oval(self.x-Person.radius, self.y-Person.radius, self.x+Person.radius, self.y+Person.radius, fill=self.color)
        self.lastMove = [0,random.random()*360]
        self.health = 0 #0 is healthy, 1 is infected, and 2 is clear
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
