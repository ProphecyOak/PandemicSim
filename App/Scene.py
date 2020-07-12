from Person import *
from xtraFunctions import *
import tkinter
import random


class Scene:
    def __init__(self, width=500, height=500, pplCount=50):
        if width < 50:
            width = 50
        self.width = width
        if height < 50:
            height = 50
        self.height = height

        self.pplCount = pplCount
        self.moving = 0
        self.master = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.master, width=width, height=height)
        self.canvas.grid(rowspan=height//10)
        self.buttonInit()

        self.pplListMaker()

    def buttonInit(self):
        self.mover = tkinter.Button(self.master, text="Move", command=self.movement)
        self.mover.grid(row=0,column=1)
        self.moveChange = tkinter.Button(self.master, text="Start", command=self.changeMoving)
        self.moveChange.grid(row=1,column=1)
        self.reseter = tkinter.Button(self.master, text="Reset", command=self.pplListMaker)
        self.reseter.grid(row=2,column=1)
        self.closer = tkinter.Button(self.master, text="Close", command=self.master.destroy)
        self.closer.grid(row=3,column=1)
        self.infect = tkinter.Button(self.master, text="Infect", command=self.infection)
        self.infect.grid(row=4,column=1)

    def pplListMaker(self):
        self.canvas.delete("all")
        self.pplList = []
        self.infectedPplList = []
        self.deadPplList = []
        self.recoveredPplList = []
        for x in range(self.pplCount):
            self.pplList.append(Person(self.canvas, self.width, self.height))

    def movement(self, times=1, mode=0):
        if mode == 0:
            for x in self.pplList:
                magnitude = 10
                angle = [radians(random.randint(0,360)), x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1]]
                choseAngle = random.choice(angle)

                coords = vectorToCoords(magnitude, choseAngle, self, x)

                self.canvas.move(x.dot, *coords)
                curCoords = self.canvas.coords(x)
                x.moveUpdate([coords[0]+x.x,coords[1]+x.y])
                x.lastMove = [magnitude,choseAngle]
            for x in self.recoveredPplList:
                magnitude = 10
                angle = [radians(random.randint(0,360)), x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1]]
                choseAngle = random.choice(angle)

                coords = vectorToCoords(magnitude, choseAngle, self, x)

                self.canvas.move(x.dot, *coords)
                curCoords = self.canvas.coords(x)
                x.moveUpdate([coords[0]+x.x,coords[1]+x.y])
                x.lastMove = [magnitude,choseAngle]
        self.infectedMove(mode)
        self.recovery()

    def infectedMove(self, mode):
        if mode == 0:
            newlyInfected = []
            for x in self.infectedPplList:
                magnitude = 10
                angle = [radians(random.randint(0,360)), x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1]]
                choseAngle = random.choice(angle)

                coords = vectorToCoords(magnitude, choseAngle, self, x)

                self.canvas.move(x.dot, *coords)
                x.moveUpdate([coords[0]+x.x,coords[1]+x.y])
                x.lastMove = [magnitude,choseAngle]
                for y in self.pplList:
                    if x.distanceBetween(y) < Person.radius*2:# and random.randint(0,100) < 90:
                        y.colorChange(self.canvas,1)
                        self.pplList.remove(y)
                        newlyInfected.append(y)
            self.infectedPplList += newlyInfected

    def changeMoving(self):
        self.moving = [1,0][self.moving]
        self.moveChange.config(text=["Start","Stop"][self.moving])
        self.master.update()

    def infection(self):
        self.infectedPplList.append(Person(self.canvas, self.width, self.height))
        self.infectedPplList[-1].colorChange(self.canvas,1)

    def recovery(self):
        for p in self.infectedPplList:
            if random.randint(0,99) in [0]:
                p.recoveryTime -= 1
            else:
                p.recoveryTime += 1
            if p.recoveryTime > 15:
                p.colorChange(self.canvas, 2)
                self.infectedPplList.remove(p)
                self.recoveredPplList.append(p)
            elif p.recoveryTime == -1:
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
