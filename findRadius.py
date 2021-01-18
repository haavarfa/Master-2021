import math
def findRadius(filename, snapshots, lines):
    j = 0
    f = open(filename, "r")
    
    vol = 0
    
    data = f.readlines()
    for i in range(len(data)):
        if len(data[i].split(' ')) == lines:
            vol = vol + float(data[i].split(' ')[5])
    
    vol = vol/snapshots

    radius = (vol*3/(4*math.pi))**(1/3)

    f.close()
    return radius