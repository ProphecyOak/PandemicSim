from math import *


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
