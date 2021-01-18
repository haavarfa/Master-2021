#Makes one file from several smaller ones

def oneBigFile(bigfile, *args):
    newfile = open(bigfile, "w+")
    for arg in args:
        currentfile = open(arg, "r")
        data = currentfile.readlines()
        for i in range (len(data)):
            newfile.write(data[i])
        currentfile.close()
    newfile.close()