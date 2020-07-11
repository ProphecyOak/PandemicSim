import tkinter
import random
from math import *
import numpy
normalDist = numpy.random.normal


def vectorToCoords(magnitude, angle, scene, dot):
    curCoords = scene.canvas.coords(dot.dot)
    deltCoords = []
    if curCoords[0] < magnitude:
        deltCoords.append(10)
    elif curCoords[0] > scene.width-magnitude:
        deltCoords.append(-10)
    else:
        deltCoords.append(magnitude*cos(angle))
    if curCoords[1] < magnitude:
        deltCoords.append(10)
    elif curCoords[1] > scene.height-magnitude:
        deltCoords.append(-magnitude)
    else:
        deltCoords.append(magnitude*sin(angle))
    scene.canvas.create_line(*curCoords,deltCoords[0]+curCoords[0],
        deltCoords[1]+curCoords[1],fill=dot.color)
    return deltCoords

class Person:
    num = 0
    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        colorList = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
        self.color = colorList[Person.num%6]
        self.dot = can.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, fill=self.color)
        self.lastMove = [0,random.random()*360]
        Person.num += 1


class Scene:
    def __init__(self, width=500, height=500, pplCount=50):
        self.master = tkinter.Tk()
        if width < 50:
            width = 50
        self.width = width
        if height < 50:
            height = 50
        self.height = height
        self.canvas = tkinter.Canvas(self.master, width=width, height=height)
        self.reseter = tkinter.Button(self.master, text="Reset", command=self.pplListMaker)
        self.reseter.grid(column=2)
        self.closer = tkinter.Button(self.master, text="Close", command=self.master.destroy)
        self.closer.grid(column=2)
        self.mover = tkinter.Button(self.master, text="Move", command=self.movement)
        self.mover.grid(column=2)
        self.canvas.grid()
        self.pplCount = pplCount
        self.pplListMaker()
        #self.master.mainloop()

    def pplListMaker(self):
        self.canvas.delete("all")
        self.pplList = []
        for x in range(self.pplCount):
            self.pplList.append(Person(self.canvas, self.width, self.height))

    def movement(self, times=1, mode=0):
        if mode == 0:
            for x in self.pplList:
                magnitude = 10#random.randint(0,30)
                angle = radians(random.randint(0,360))
                coords = vectorToCoords(magnitude, angle, self, x)
                self.canvas.move(x.dot, *coords)
                x.lastMove = coords
