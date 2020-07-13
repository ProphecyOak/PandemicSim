import tkinter


configFile = open("config.txt")
configText = configFile.readlines()
configFile.close()

class SideGraph:
    exec(configText[0])

    def __init__(self, master,row,width=1000,height=200):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = tkinter.Canvas(self.master,width=width,height=height)
        self.canvas.grid(row=row+1,columnspan=3)
        self.curX = 10
        self.plotPoints = []
        self.end = 0
    def plotData(self, healthy, infected, recovered, dead):
        barWidth = 10
        spacing = 2
        if self.curX > self.width or self.end == 1:
            for x in self.plotPoints[0]:
                self.canvas.delete(x)
            for x in self.plotPoints:
                for y in x:
                    self.canvas.move(y,-barWidth-spacing,0)
            self.plotPoints.pop(0)
            if self.end != 1:
                self.curX = self.width-barWidth
                self.end = 1
        startX = self.curX
        endX = self.curX + barWidth

        height = self.height-20

        total = healthy + infected + recovered + dead
        healthyPer = healthy/total
        infectedPer = infected/total
        recoveredPer = recovered/total
        deadPer = dead/total

        healthyPx = round(healthyPer*height,0)
        infectedPx = round(infectedPer*height,0)
        recoveredPx = round(recoveredPer*height,0)
        deadPx = round(deadPer*height,0)

        self.plotPoints.append([self.canvas.create_rectangle(startX, 10, endX, deadPx+10, fill=SideGraph.colors[3], outline=SideGraph.colors[3]), self.canvas.create_rectangle(startX, deadPx+10, endX, deadPx+recoveredPx+10, fill=SideGraph.colors[2], outline=SideGraph.colors[2]), self.canvas.create_rectangle(startX, deadPx+recoveredPx+10, endX, deadPx+recoveredPx+healthyPx+10, fill=SideGraph.colors[0], outline=SideGraph.colors[0]), self.canvas.create_rectangle(startX, deadPx+recoveredPx+healthyPx+10, endX, height+10, fill=SideGraph.colors[1], outline=SideGraph.colors[1])])
        if self.end == 0:
            self.curX += barWidth+spacing
