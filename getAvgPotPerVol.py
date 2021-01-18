def getAvgs(potfile, densfile):

    f = open(potfile, "r")
    g = open(densfile, "r")

    pot_data = f.readlines()
    dens_data = g.readlines()

    pot = 0
    vol = 0
    dens = 0
    

    for i in range(len(dens_data)):
        dens += float(dens_data[i])
        vol += 1/float(dens_data[i])
    for i in range(len(pot_data)):
        pot += float(pot_data[i])
    
    dens = dens/len(dens_data)

    pot= pot/vol

    return dens, pot