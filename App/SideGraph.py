import tkinter


configFile = open("config.txt")
configText = configFile.read()
configFile.close()

class sideGraph:
    exec(configText)

    def __init__(self, master):
        self.master = master
        
