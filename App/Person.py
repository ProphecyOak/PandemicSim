import random
from math import *


class Person:
    num = 0
    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = "green"
        self.dot = can.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, fill=self.color)
        self.lastMove = [0,random.random()*360]
        self.health = 0 #0 is healthy, 1 is infected, and 2 is clear
        Person.num += 1

    def colorChange(self, can, Grp):
        self.color = ["green","red"][Grp]
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
