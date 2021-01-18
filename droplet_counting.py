#Droplet counting algorithm, can be added to the Voronoi density-neighbor method script.
#Calculates droplet amount at the first snapshot

num_droplets = np.zeros(50000)
num_drop = 0

n = 0
drop = 0
l = 0
x = 1
counting = 0
increasing = True
while l < len(surf_array[0]):
    print("l is %i" % l)
    drop += 1
    first = False
    n = 0
    drop_size = 0
    increasing = True
    while first == False:
        if num_droplets[int(surf_array[0][n])-1] == 0:
            num_droplets[int(surf_array[0][n])-1] = drop
            first = True
            l += 1
        else:
            n += 1
    while increasing == True:
        increasing = False
        print("%ist time checking." % x)
        x += 1
        counting = 0
        for i in range(len(neighbor_data)):
            if (len(neighbor_data[i].split(' '))) == 5 and neighbor_data[i].split(' ')[0] != "ITEM:":
                counting += 1
                if int(neighbor_data[i].split(' ')[1]) in surf_array[0] and int(neighbor_data[i].split(' ')[2]) in surf_array[0] and num_droplets[int(neighbor_data[i].split(' ')[1])-1] == drop and num_droplets[int(neighbor_data[i].split(' ')[2])-1] != drop: 
                    num_droplets[int(neighbor_data[i].split(' ')[2])-1] = drop
                    increasing = True
                    l += 1
                    drop_size += 1
                if (len(neighbor_data[i+1].split(' '))) != 5:
                    break
    if drop_size >= 10:
        num_drop += 1

print("Droplet amount is %i" % num_drop)