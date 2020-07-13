import random
from math import *


configFile = open("config.txt")
configText = configFile.readlines()
configFile.close()

class Person:
    num = 0
    exec(configText[0])
    exec(configText[1])
    exec(configText[2])

    def __init__(self, can, xMax, yMax,socialDist=0):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = Person.colors[0]
        self.lightColor = Person.lightColors[0]
        self.dot = can.create_oval(self.x-Person.radius, self.y-Person.radius, self.x+Person.radius, self.y+Person.radius, fill=self.color, outline="")
        self.outerCircle = can.create_oval(self.x-Person.radius*3, self.y-Person.radius*3, self.x+Person.radius*3, self.y+Person.radius*3, outline = self.lightColor, width=2, state=["normal","hidden"][socialDist])
        self.lastMove = [0,random.random()*360]
        self.health = 0 #0 is healthy, 1 is infected, 2 is clear, and 3 is dead
        self.recoveryTime = 0
        self.rebelliousness = random.randint(0, 7)
        self.symptomatic = 0
        self.immunocompromisedMultiplier = 1
        immunocompromised = random.randint(1,100)
        if immunocompromised in range(0,4):
            self.immunocompromisedMultiplier = 12
        probability = random.randint(1, 100)
        if probability <= 7:
            self.susceptibility = 0
        elif probability > 7 and probability <= 21:
            self.susceptibility = 1
        elif probability > 21 and probability <= 62:
            self.susceptibility = 2
        elif probability > 62 and probability <= 82:
            self.susceptibility = 3
        elif probability > 82 and probability <= 95:
            self.susceptibility = 4
        else:
            self.susceptibility = 5
        Person.num += 1

    def colorChange(self, can, Grp=1):
        self.color = Person.colors[Grp]
        can.itemconfig(self.dot, fill=self.color)
        if Grp < 3:
            self.lightColor = Person.lightColors[Grp]
            can.itemconfig(self.outerCircle, outline=self.lightColor, width=2)
        elif Grp > 3:
            self.lightColor = Person.lightColors[Grp-1]
            can.itemconfig(self.outerCircle, outline=self.lightColor, width=2)
        else:
            can.delete(self.outerCircle)
        self.health = Grp

    def distanceBetween(self, other):
        xDiff = abs(self.x-other.x)
        yDiff = abs(self.y-other.y)
        distBtwn = sqrt(xDiff**2 + yDiff**2)
        return distBtwn

    def moveUpdate(self,coords):
        self.x = coords[0]
        self.y = coords[1]
