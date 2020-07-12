import tkinter


configFile = open("config.txt")
configText = configFile.readlines()
configFile.close()

class SideGraph:
    exec(configText[0])

    def __init__(self, master,row,width=500,height=200):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = tkinter.Canvas(self.master,width=width,height=height)
        self.canvas.grid(row=row+1)
        self.curX = 10
        self.plotPoints = []
    def plotData(self, healthy, infected, recovered, dead):
        if self.curX > self.width-10:
            for x in self.plotPoints[0]:
                self.canvas.delete(x)
            for x in self.plotPoints:
                for y in x:
                    self.canvas.move(y,-15,0)
            self.plotPoints.pop(0)
            self.curX = self.width-10
        startX = self.curX
        endX = self.curX + 10
        total = healthy + infected + recovered + dead
