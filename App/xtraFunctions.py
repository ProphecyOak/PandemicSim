from math import *


configFile = open("config.txt")
configText = configFile.readlines()
configFile.close()
exec(configText[1])

def vectorToCoords(magnitude, angle, scene, dot):
    global radiius

    curCoords = [dot.x,dot.y]
    deltCoords = []
    if curCoords[0] < radius*3:
        deltCoords.append(magnitude)
    elif curCoords[0] > scene.width-radius*3:
        deltCoords.append(-magnitude)
    else:
        deltCoords.append(magnitude*cos(angle))
    if curCoords[1] < radius*3:
        deltCoords.append(magnitude)
    elif curCoords[1] > scene.height-radius*3:
        deltCoords.append(-magnitude)
    else:
        deltCoords.append(magnitude*sin(angle))
    #scene.canvas.create_line(curCoords[0]+5, curCoords[1]+5, deltCoords[0]+curCoords[0]+5, deltCoords[1]+curCoords[1]+5,fill=dot.color)
    return deltCoords
