from Person import *
from SideGraph import *
from xtraFunctions import *
import tkinter
import random


configFile = open("config.txt")
configText = configFile.readlines()
configFile.close()

class Scene:
    exec(configText[3])
    def __init__(self, width=500, height=500, pplCount=50, socialDist=0, socialStrict=8, quarantineStrict=3):
        if width < 50:
            width = 50
        self.width = width
        if height < 50:
            height = 50
        self.height = height

        self.pplCount = pplCount
        self.socialDist = socialDist
        self.socialStrict = socialStrict
        self.quarantineStrict = quarantineStrict
        self.moving = 0
        self.master = tkinter.Tk()
        self.master.configure(bg=Scene.backColor[1])
        self.recoveryLength = 25
        self.moveCount = -1

        self.canvas = tkinter.Canvas(self.master, width=width, height=height, bg=Scene.backColor[0], highlightbackground=Scene.backColor[3])
        self.canvas.grid(rowspan=height//10)
        self.spacer = tkinter.Label(self.master,bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.spacer.grid(row=height//10,column=0)

        self.sideGraph = SideGraph(self.master,height//10+1)

        self.buttonInit()
        self.textInit()
        self.configInit()

        self.pplListMaker()

    def buttonInit(self):
        self.mover = tkinter.Button(self.master, text="Move", command=self.movement, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.mover.grid(row=0,column=1)
        self.moveChange = tkinter.Button(self.master, text="Start", command=self.changeMoving, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.moveChange.grid(row=1,column=1)
        self.reseter = tkinter.Button(self.master, text="Reset", command=self.pplListMaker, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.reseter.grid(row=2,column=1)
        self.closer = tkinter.Button(self.master, text="Close", command=self.master.destroy, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.closer.grid(row=3,column=1)
        self.infect = tkinter.Button(self.master, text="Infect", command=self.infection, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.infect.grid(row=4,column=1)
        self.infect = tkinter.Button(self.master, text="Distance!", command=self.commenceDistancing, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.infect.grid(row=5,column=1)
        self.lastButtonRow = 5

    def textInit(self):
        x = self.lastButtonRow-1
        self.healthyText = tkinter.Label(self.master, text="Healthy:", bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.healthyText.grid(row=x+2,column=1)
        self.healthyNum = tkinter.Label(self.master, text=self.pplCount, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.healthyNum.grid(row=x+3,column=1)
        self.infectedText = tkinter.Label(self.master, text="Infected:", bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.infectedText.grid(row=x+4,column=1)
        self.infectedNum = tkinter.Label(self.master, text=0, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.infectedNum.grid(row=x+5,column=1)
        self.recoveredText = tkinter.Label(self.master, text="Recovered:", bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.recoveredText.grid(row=x+6,column=1)
        self.recoveredNum = tkinter.Label(self.master, text=0, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.recoveredNum.grid(row=x+7,column=1)
        self.deadText = tkinter.Label(self.master, text="Dead:", bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.deadText.grid(row=x+8,column=1)
        self.deadNum = tkinter.Label(self.master, text=0, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.deadNum.grid(row=x+9,column=1)
        self.moveText = tkinter.Label(self.master, text="Moves:", bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.moveText.grid(row=x+10,column=1)
        self.moveNum = tkinter.Label(self.master, text=0, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.moveNum.grid(row=x+11,column=1)
        self.lastTextRow = 11

    def configInit(self):
        self.socialStrictVar = tkinter.StringVar()
        self.socialStrictText = tkinter.Button(self.master, text="Social Distancing Strictness:", command=self.changeSocialStrict, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.socialStrictText.grid(row=0,column=2)
        self.socialStrictField = tkinter.Entry(self.master, textvariable=self.socialStrictVar, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.socialStrictField.grid(row=1,column=2)

        self.quarantineStrictVar = tkinter.StringVar()
        self.quarantineStrictText = tkinter.Button(self.master, text="Quarantine Strictness:", command=self.changeQuarantineStrict, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.quarantineStrictText.grid(row=2,column=2)
        self.quarantineStrictField = tkinter.Entry(self.master, textvariable=self.quarantineStrictVar, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.quarantineStrictField.grid(row=3,column=2)

        self.popSizeVar = tkinter.StringVar()
        self.popSizeText = tkinter.Button(self.master, text="Population Size:", command=self.changePopSize, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.popSizeText.grid(row=4,column=2)
        self.popSizeField = tkinter.Entry(self.master, textvariable=self.popSizeVar, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.popSizeField.grid(row=5,column=2)

        self.radiusVar = tkinter.StringVar()
        self.radiusText = tkinter.Button(self.master, text="Person Size:", command=self.changeRadius, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.radiusText.grid(row=6,column=2)
        self.radiusField = tkinter.Entry(self.master, textvariable=self.radiusVar, bg=Scene.backColor[1], fg=Scene.backColor[2])
        self.radiusField.grid(row=7,column=2)

    def pplListMaker(self):
        self.canvas.delete("all")
        self.pplList = []
        self.infectedPplList = []
        self.deadPplList = []
        self.recoveredPplList = []
        for x in range(self.pplCount):
            self.pplList.append(Person(self.canvas, self.width, self.height, socialDist=self.socialDist))
        self.moveCount = -1
        self.movement()

    def movement(self, times=1, mode=0):
        self.allPplList = self.pplList + self.infectedPplList + self.recoveredPplList
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
        self.moveCount += 1
        self.moveNum.config(text=self.moveCount)

    def infectedMove(self, mode):
        if mode == 0:
            newlyInfected = []
            for x in self.infectedPplList:
                if x.symptomatic == 1:
                    x.colorChange(self.canvas,4)
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
                            if random.random() <= .35:
                                y.symptomatic = 1
                            newlyInfected.append(y)
                elif x.symptomatic == 0:
                    if x.rebelliousness > self.quarantineStrict:
                        magnitude = x.rebelliousness
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
                                if random.random() <= .35:
                                    y.symptomatic = 1
                                newlyInfected.append(y)
            self.infectedPplList += newlyInfected
            self.healthyNum.config(text=len(self.pplList))
            self.infectedNum.config(text=len(self.infectedPplList))
            self.deadNum.config(text=len(self.deadPplList))

    def changeMoving(self):
        self.moving = [1,0][self.moving]
        self.moveChange.config(text=["Start","Stop"][self.moving])
        self.master.update()

    def infection(self):
        self.infectedPplList.append(Person(self.canvas, self.width, self.height, socialDist=self.socialDist))
        self.infectedNum.config(text=len(self.infectedPplList))
        self.infectedPplList[-1].colorChange(self.canvas,1)
        self.infectedPplList[-1].symptomatic = 1

    def recovery(self):
        for p in self.infectedPplList:
            #if random.randint(1,1000*self.recoveryLength) in range(1,15) and p.susceptibility > 2:
            if p.susceptibility == 0 and random.randint(1,1000000*self.recoveryLength) in range(1,17*p.immunocompromisedMultiplier):
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
            elif p.susceptibility == 1 and random.randint(1,10000000*self.recoveryLength) in range(1,33*p.immunocompromisedMultiplier):
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
            elif p.susceptibility == 2 and random.randint(1,1000000*self.recoveryLength) in range(1,93*p.immunocompromisedMultiplier):
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
            elif p.susceptibility == 3 and random.randint(1,10000*self.recoveryLength) in range(1,15*p.immunocompromisedMultiplier):
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
            elif p.susceptibility == 4 and random.randint(1,1000*self.recoveryLength) in range(1,56*p.immunocompromisedMultiplier):
                p.colorChange(self.canvas, 3)
                self.infectedPplList.remove(p)
                self.deadPplList.append(p)
            else:
                p.recoveryTime += 1
            if p.recoveryTime > self.recoveryLength:
                p.colorChange(self.canvas, 2)
                self.infectedPplList.remove(p)
                self.recoveredPplList.append(p)
        self.recoveredNum.config(text=len(self.recoveredPplList))
        self.infectedNum.config(text=len(self.infectedPplList))

    def possibleCollision(self):
        for item in self.allPplList:
            for indx in range(self.allPplList.index(item)+1, len(self.allPplList)):
                if item.distanceBetween(self.allPplList[indx])<=6*Person.radius:
                    if item.rebelliousness + self.allPplList[indx].rebelliousness < self.socialStrict and self.socialDist == 0:#bounce off
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

    def changeSocialStrict(self):
        self.socialStrict = int(self.socialStrictVar.get())
    def changeQuarantineStrict(self):
        self.quarantineStrict = int(self.quarantineStrictVar.get())
    def changePopSize(self):
        self.pplCount = int(self.popSizeVar.get())
        self.pplListMaker()
    def changeRadius(self):
        Person.radius = int(self.radiusVar.get())
        self.pplListMaker()

    def commenceDistancing(self):
        self.socialDist = [1,0][self.socialDist]
        for x in self.allPplList:
            self.canvas.itemconfig(x.outerCircle, state=["normal","hidden"][self.socialDist])
