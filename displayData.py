import tkinter

class Scene:
    def __init__(self, width=500, height=500):
        self.master = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.master, width=width, height=height)
        self.canvas.pack()
