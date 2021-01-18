def getPressure(file):
    f = open(file, "r")
    data = f.readlines()

    vol = 0
    stress = 0

    for i in range(len(data)):
        if len(data[i].split(' ')) == 17:
            vol += float(data[i].split(' ')[5])
            stress += (float(data[i].split(' ')[10])+float(data[i].split(' ')[11])+float(data[i].split(' ')[12]))
            
    pressure =  (-stress) / (3*vol)
    f.close()
    return pressure