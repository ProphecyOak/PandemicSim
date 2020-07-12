from Person import *
from SideGraph import *
from xtraFunctions import *
import tkinter
import random


class Scene:
    def __init__(self, width=500, height=500, pplCount=50,socialDist=0):
        if width < 50:
            width = 50
        self.width = width
        if height < 50:
            height = 50
        self.height = height

        self.pplCount = pplCount
        self.socialDist = socialDist
        self.moving = 0
        self.master = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.master, width=width, height=height)
        self.canvas.grid(rowspan=height//10)

        self.sideGraph = SideGraph(self.master,height//10)

        self.buttonInit()
        self.textInit()

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
        self.lastButtonRow = 4

    def textInit(self):
        x = self.lastButtonRow-1
        self.healthyText = tkinter.Label(self.master, text="Healthy:")
        self.healthyText.grid(row=x+2,column=1)
        self.healthyNum = tkinter.Label(self.master, text=self.pplCount)
        self.healthyNum.grid(row=x+3,column=1)
        self.infectedText = tkinter.Label(self.master, text="Infected:")
        self.infectedText.grid(row=x+4,column=1)
        self.infectedNum = tkinter.Label(self.master, text=0)
        self.infectedNum.grid(row=x+5,column=1)
        self.recoveredText = tkinter.Label(self.master, text="Recovered:")
        self.recoveredText.grid(row=x+6,column=1)
        self.recoveredNum = tkinter.Label(self.master, text=0)
        self.recoveredNum.grid(row=x+7,column=1)
        self.deadText = tkinter.Label(self.master, text="Dead:")
        self.deadText.grid(row=x+8,column=1)
        self.deadNum = tkinter.Label(self.master, text=0)
        self.deadNum.grid(row=x+9,column=1)

    def pplListMaker(self):
        self.canvas.delete("all")
        self.pplList = []
        self.infectedPplList = []
        self.deadPplList = []
        self.recoveredPplList = []
        for x in range(self.pplCount):
            self.pplList.append(Person(self.canvas, self.width, self.height, socialDist=self.socialDist))

    def movement(self, times=1, mode=0):
        if mode == 0:
            for x in self.pplList:
                magnitude = 10
                angle = [radians(random.randint(0,360)), x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1]]
                choseAngle = random.choice(angle)

                coords = vectorToCoords(magnitude, choseAngle, self, x)

                self.canvas.move(x.dot, *coords)
                self.canvas.move(x.outerCircle, *coords)
                curCoords = self.canvas.coords(x)
                x.moveUpdate([coords[0]+x.x,coords[1]+x.y])
                x.lastMove = [magnitude,choseAngle]
            for x in self.recoveredPplList:
                magnitude = 10
                angle = [radians(random.randint(0,360)), x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1]]
                choseAngle = random.choice(angle)

                coords = vectorToCoords(magnitude, choseAngle, self, x)

                self.canvas.move(x.dot, *coords)
                self.canvas.move(x.outerCircle, *coords)
                curCoords = self.canvas.coords(x)
                x.moveUpdate([coords[0]+x.x,coords[1]+x.y])
                x.lastMove = [magnitude,choseAngle]
        self.possibleCollision()
        self.infectedMove(mode)
        self.recovery()
        self.sideGraph.plotData(len(self.pplList),len(self.infectedPplList),len(self.recoveredPplList),len(self.deadPplList))

    def infectedMove(self, mode):
        if mode == 0:
            newlyInfected = []
            for x in self.infectedPplList:
                magnitude = 10
                angle = [radians(random.randint(0,360)), x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1], x.lastMove[1]]
                choseAngle = random.choice(angle)

                coords = vectorToCoords(magnitude, choseAngle, self, x)

                self.canvas.move(x.dot, *coords)
                self.canvas.move(x.outerCircle, *coords)
                x.moveUpdate([coords[0]+x.x,coords[1]+x.y])
                x.lastMove = [magnitude,choseAngle]
                for y in self.pplList:
                    if x.distanceBetween(y) < Person.radius*2:# and random.randint(0,100) < 90:
                        y.colorChange(self.canvas,1)
                        self.pplList.remove(y)
                        newlyInfected.append(y)
            self.healthyNum.config(text=len(self.pplList))
            self.infectedNum.config(text=len(self.infectedPplList))
            self.deadNum.config(text=len(self.deadPplList))
            self.infectedPplList += newlyInfected

    def changeMoving(self):
        self.moving = [1,0][self.moving]
        self.moveChange.config(text=["Start","Stop"][self.moving])
        self.master.update()

    def infection(self):
        self.infectedPplList.append(Person(self.canvas, self.width, self.height, socialDist=self.socialDist))
        self.infectedNum.config(text=len(self.infectedPplList))
        self.infectedPplList[-1].colorChange(self.canvas,1)

    def recovery(self):
        for p in self.infectedPplList:
            if random.randint(0,99) in [0]:
                p.recoveryTime -= 10
            else:
                p.recoveryTime += 1
            if p.recoveryTime > 25:
                p.colorChange(self.canvas, 2)
                self.infectedPplList.remove(p)
                self.recoveredPplList.append(p)
            elif p.recoveryTime == -1:
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
        self.recoveredNum.config(text=len(self.recoveredPplList))
        self.infectedNum.config(text=len(self.infectedPplList))

    def possibleCollision(self):
        self.allPplList = self.pplList + self.infectedPplList + self.recoveredPplList
        for item in self.allPplList:
            for indx in range(self.allPplList.index(item)+1, len(self.allPplList)):
                if item.distanceBetween(self.allPplList[indx])<=6*Person.radius:
                    if item.rebelliousness + self.allPplList[indx].rebelliousness < 20:#bounce off
                        newAngle = item.lastMove[1]+radians(180)
                        choseAngle = newAngle
                        magnitude = 10
                        coords = vectorToCoords(magnitude, choseAngle, self, item)
                        self.canvas.move(item.dot, *coords)
                        self.canvas.move(item.outerCircle, *coords)
                        curCoords = self.canvas.coords(item)
                        item.moveUpdate([coords[0]+item.x,coords[1]+item.y])
                        item.lastMove = [magnitude,choseAngle]
                    break
                    #else:
                        #don't course correct
