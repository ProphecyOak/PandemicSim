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
        startY = self.height-10
        endY = 10
        total = healthy + infected + recovered + dead
        healthy = infected/total
        infected = healthy/total
        recovered = recovered/total
        dead = dead/total
        healthyY = self.height-10-(self.height-20)*healthy
        infectedY = healthyY-(self.height-20)*infected
        recoveredY = infectedY-(self.height-20)*recovered
        print("\n"+str(healthy)[:4],str(infected)[:4],str(recovered)[:4],str(dead)[:4],"   ",str(total)[:4])
        print(str(healthyY)[:6],str(infectedY)[:6],str(recoveredY)[:6])
        self.plotPoints.append([self.canvas.create_rectangle(startX,startY,endX,healthyY,fill=SideGraph.colors[1]), self.canvas.create_rectangle(startX, healthyY, endX, infectedY,fill=SideGraph.colors[0]), self.canvas.create_rectangle(startX, infectedY, endX, recoveredY,fill=SideGraph.colors[2]), self.canvas.create_rectangle(startX, recoveredY, endX, endY,fill=SideGraph.colors[3])])
        self.curX += 15
