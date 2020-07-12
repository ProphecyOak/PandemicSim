import random


class Person:
    num = 0
    def __init__(self, can, xMax, yMax):
        self.x = random.randint(20,xMax-20)
        self.y = random.randint(20,yMax-20)
        self.color = "green"
        self.dot = can.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, fill=self.color)
        self.lastMove = [0,random.random()*360]
        self.health = 0
        Person.num += 1

    def colorChange(self, can):
        self.color = "red"
        can.itemconfig(self.dot, fill=self.color)
        self.health = 1
