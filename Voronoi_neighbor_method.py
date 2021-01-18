import numpy as np

main = open([MAIN DUMP FILE], "r")
neighbor = open([NEIGHBOR DUMP FILE], "r")

voro_data = main.readlines()
neighbor_data = neighbor.readlines()

length = 17
iterations = 5

gas_limit = 0.45
liquid_limit = 0.55


k = 0


voro_area = 0
voro_area_gas = 0
voro_area_liquid = 0
j = 0

surf_array = []
true_interfacial_list = []

gas_array = []
liquid_array = []

gas_list = []
liquid_list = []

step = 1
num_particles = 0

for i in range(len(voro_data)):
    if (len(voro_data[i].split(' '))) == length:
        if step == 1:
            num_particles += 1
        if (1/float(voro_data[i].split( ' ')[5])) <= (0.03):
            gas_list.append(float(voro_data[i].split(' ')[0]))
        elif (1/float(voro_data[i].split(' ')[5])) >= (0.521):
            liquid_list.append(float(voro_data[i].split(' ')[0]))
        if i+1 == len(voro_data) or (len(voro_data[i+1].split(' '))) != length:
            gas_array.append(np.array(gas_list)) 
            gas_list = []
            liquid_array.append(np.array(liquid_list))
            liquid_list = []
            step += 1

print(num_particles)

step = 1

neighbor_steps = 0

for c in range (iterations):
    for i in range (len(neighbor_data)):
        if (len(neighbor_data[i].split(' '))) == 5 and neighbor_data[i].split(' ')[0] != "ITEM:":
            if step == 1:
                neighbor_steps += 1
            if float(neighbor_data[i].split(' ')[1]) not in gas_array[j] and float(neighbor_data[i].split(' ')[1]) not in liquid_array[j]:
                if float(neighbor_data[i].split(' ')[2]) in gas_array[j]:
                    voro_area_gas += float(neighbor_data[i].split(' ')[3])
                elif float(neighbor_data[i].split(' ')[2]) in liquid_array[j]:
                    voro_area_liquid += float(neighbor_data[i].split(' ')[3])
                voro_area += float(neighbor_data[i].split(' ')[3])
            if i+1 == len(neighbor_data) or neighbor_data[i].split(' ')[1] != neighbor_data[i+1].split(' ')[1]:
                if (float(neighbor_data[i].split(' ')[1]) not in liquid_array[j]) and (float(neighbor_data[i].split(' ')[1]) not in gas_array[j]) and voro_area != 0 and (voro_area_gas / voro_area) > gas_limit:
                    gas_array[j] = np.append(gas_array[j], float(neighbor_data[i].split(' ')[1]))
                elif (float(neighbor_data[i].split(' ')[1]) not in liquid_array[j]) and (float(neighbor_data[i].split(' ')[1]) not in gas_array[j]) and voro_area != 0 and (voro_area_liquid / voro_area) > liquid_limit:
                    liquid_array[j] = np.append(liquid_array[j], float(neighbor_data[i].split(' ')[1]))
                if c == iterations-1 and float(neighbor_data[i].split(' ')[1]) not in liquid_array[j] and float(neighbor_data[i].split(' ')[1]) not in gas_array[j]:
                    true_interfacial_list.append(float(neighbor_data[i].split(' ')[1]))
                voro_area = 0
                voro_area_gas = 0
                voro_area_liquid = 0
                step += 1
            if i+1 == len(neighbor_data) or neighbor_data[i+1].split(' ')[0] == "ITEM:":
                if c == iterations-1:
                    surf_array.append(np.array(true_interfacial_list))
                    true_interfacial_list = []
                j += 1
    j = 0


int_dens = open([INTERFACE_DENSITY_FILE], "w+")
int_pot = open([INTERFACE_POTENER_FILE], "w+")


interface_file = open([INTERFACE_VISUALIZATION_FILE], "w+")
liquid_file = open([LIQUID_DATA_FILE], "w+")
gas_file = open([VAPOR_DATA_FILE]], "w+")

gas_dens = open([VAPOR_DENSITY_FILE], "w+")
gas_pot = open([VAPOR_POTENER_FILE]], "w+")

liq_dens = open([LIQUID_DENSITY_FILE], "w+")
liq_pot = open([LIQUID_POTENER_FILE], "w+")


liq_vol = 0
gas_vol = 0

total_liq_vol = 0
total_gas_vol = 0

liq_stress = 0
gas_stress = 0

liq_press = [0 for i in range(201)]
gas_press = [0 for i in range(201)]

for i in range (len(voro_data)):
    if (len(voro_data[i].split(' '))) == length:
        densfile.write("%s \n" % str(1/float(voro_data[i].split(' ')[5])))
        if float(voro_data[i].split(' ')[0]) in surf_array[k]:
            int_dens.write("%s \n" % str(1/float(voro_data[i].split(' ')[5])))
            int_pot.write("%s \n" % voro_data[i].split(' ')[8])
            interface_file.write("%s 2 %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n" % (voro_data[i].split(' ')[0], voro_data[i].split(' ')[2], voro_data[i].split(' ')[3], voro_data[i].split(' ')[4], voro_data[i].split(' ')[5], voro_data[i].split(' ')[6], voro_data[i].split(' ')[7], voro_data[i].split(' ')[8], voro_data[i].split(' ')[9], voro_data[i].split(' ')[10], voro_data[i].split(' ')[11], voro_data[i].split(' ')[12], voro_data[i].split(' ')[13], voro_data[i].split(' ')[14], voro_data[i].split(' ')[15]))
        elif (float(voro_data[i].split(' ')[0])) in liquid_array[k]:
            interface_file.write("%s 3 %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n" % (voro_data[i].split(' ')[0], voro_data[i].split(' ')[2], voro_data[i].split(' ')[3], voro_data[i].split(' ')[4], voro_data[i].split(' ')[5], voro_data[i].split(' ')[6], voro_data[i].split(' ')[7], voro_data[i].split(' ')[8], voro_data[i].split(' ')[9], voro_data[i].split(' ')[10], voro_data[i].split(' ')[11], voro_data[i].split(' ')[12], voro_data[i].split(' ')[13], voro_data[i].split(' ')[14], voro_data[i].split(' ')[15]))
            liq_pot.write("%s \n" % voro_data[i].split(' ')[8])
            liquid_file.write("%s" % voro_data[i])
            liq_dens.write("%s \n" % str(1/float(voro_data[i].split(' ')[5])))
            liq_vol += float(voro_data[i].split(' ')[5])
            liq_stress += (float(voro_data[i].split(' ')[10])+float(voro_data[i].split(' ')[11])+float(voro_data[i].split(' ')[12]))
        else:
            interface_file.write("%s" % voro_data[i])
            gas_file.write("%s" % voro_data[i])
            gas_pot.write("%s \n" % voro_data[i].split(' ')[8])
            gas_dens.write("%s \n" % str(1/float(voro_data[i].split(' ')[5])))
            gas_vol += float(voro_data[i].split(' ')[5])
            gas_stress += (float(voro_data[i].split(' ')[10])+float(voro_data[i].split(' ')[11])+float(voro_data[i].split(' ')[12]))
        if i+1 == len(voro_data) or (len(voro_data[i+1].split(' '))) != length:
            liq_press[k] =  (-liq_stress) / (3*liq_vol)
            gas_press[k] =  (-gas_stress) / (3*gas_vol)
            total_liq_vol += liq_vol
            total_gas_vol += gas_vol
            liq_stress = 0
            gas_stress = 0
            liq_vol = 0
            gas_vol = 0
            k += 1
    else:
        interface_file.write("%s" % voro_data[i])

gas_enthalpy = 0
liquid_enthalpy = 0

k = 0


for i in range (len(voro_data)):
    if (len(voro_data[i].split(' '))) == length:
        if (float(voro_data[i].split(' ')[0])) in liquid_array[k]:
            liquid_enthalpy += float(voro_data[i].split(' ')[8]) + float(voro_data[i].split(' ')[9]) + (float(voro_data[i].split(' ')[5]) * liq_press[k])
        elif (float(voro_data[i].split(' ')[0])) in gas_array[k]:
            gas_enthalpy += float(voro_data[i].split(' ')[8]) + float(voro_data[i].split(' ')[9]) + (float(voro_data[i].split(' ')[5]) * gas_press[k])
        if i+1 == len(voro_data) or (len(voro_data[i+1].split(' '))) != length:
            k += 1

gas_enthalpy_total = gas_enthalpy/201
liquid_enthalpy_total = liquid_enthalpy/201

gas_enthalpy_pervol = gas_enthalpy/total_gas_vol
liquid_enthalpy_pervol = liquid_enthalpy/total_liq_vol

endfile = open([ENTHALPY_DATA_FILE], "a")
endfile.write("[SYSTEM] first step:\n")
endfile.write("Total gas enthalpy is %f, gas enthalpy per vol is %f\n" % (gas_enthalpy_total, gas_enthalpy_pervol))
endfile.write("Total liquid enthalpy is %f, liquid enthalpy per vol is %f\n" % (liquid_enthalpy_total, liquid_enthalpy_pervol))
