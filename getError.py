import math

def getError(mean, block):
    squared_dev = 0
    
    for i in range(len(block)):
        squared_dev += (block[i] - mean)**2
    
    variance = squared_dev/(len(block) - 1)

    std_dv = math.sqrt(variance)

    error = std_dv/math.sqrt(len(block))

    return error