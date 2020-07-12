import tkinter
import random
from math import *
import numpy
normalDist = numpy.random.normal


def vectorToCoords(magnitude, angle, scene, dot):
    curCoords = scene.canvas.coords(dot.dot)
    deltCoords = []
    if curCoords[0] < 20:
        deltCoords.append(magnitude)
    elif curCoords[0] > scene.width-20:
        deltCoords.append(-magnitude)
    else:
        deltCoords.append(magnitude*cos(angle))
    if curCoords[1] < 20:
        deltCoords.append(magnitude)
    elif curCoords[1] > scene.height-20:
        deltCoords.append(-magnitude)
    else:
        deltCoords.append(magnitude*sin(angle))
    #scene.canvas.create_line(curCoords[0]+5, curCoords[1]+5, deltCoords[0]+curCoords[0]+5, deltCoords[1]+curCoords[1]+5,fill=dot.color)
    return deltCoords

class Person:
    num = 0
    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = "Green"
        self.dot = can.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, fill=self.color)
        self.lastMove = [0,random.random()*360]
        Person.num += 1


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

        self.mover = tkinter.Button(self.master, text="Move", command=self.movement)
        self.mover.grid(row=0,column=1)
        self.moveChange = tkinter.Button(self.master, text="Start", command=self.changeMoving)
        self.moveChange.grid(row=1,column=1)
        self.reseter = tkinter.Button(self.master, text="Reset", command=self.pplListMaker)
        self.reseter.grid(row=2,column=1)
        self.closer = tkinter.Button(self.master, text="Close", command=self.master.destroy)
        self.closer.grid(row=3,column=1)

        self.pplListMaker()

    def pplListMaker(self):
        self.canvas.delete("all")
        self.pplList = []
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
                x.lastMove = [magnitude,choseAngle]

    def changeMoving(self):
        self.moving = [1,0][self.moving]
        self.moveChange.config(text=["Start","Stop"][self.moving])
