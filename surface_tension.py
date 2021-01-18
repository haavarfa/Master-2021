from findRadius import findRadius
from oneBigFile import oneBigFile
from getError import getError
from getPressure import getPressure

import os.path
from os import path

size = [SYSTEM SIZE]
#limit = 50

end_liquid = [BIG LIQUID DATA FILE]
end_gas = [BIG VAPOR DATA FILE]

liquid1 = [LIQUID DATA FILE 1]
liquid2 = [LIQUID DATA FILE 2]
liquid3 = [LIQUID DATA FILE 3]
liquid4 = [LIQUID DATA FILE 4]
liquid5 = [LIQUID DATA FILE 5]

if not path.exists(end_liquid):
    oneBigFile(end_liquid, liquid1, liquid2, liquid3, liquid4, liquid5)

gas1 = [VAPOR DATA FILE 1]
gas2 = [VAPOR DATA FILE 2]
gas3 = [VAPOR DATA FILE 3]
gas4 = [VAPOR DATA FILE 4] 
gas5 = [VAPOR DATA FILE 5]



if not path.exists(end_gas):
    oneBigFile(end_gas, gas1, gas2, gas3, gas4, gas5)

pressure_gas = getPressure(end_gas)

pressure_liq = getPressure(end_liquid)



radius = findRadius(end_liquid, 1005, 17)


rad_block = [findRadius(liquid1, 201, 17), findRadius(liquid2, 201, 17), findRadius(liquid3, 201, 17), findRadius(liquid4, 201, 17), findRadius(liquid5, 201, 17)]
rad_error = getError(radius, rad_block)

#inv_rad_block = [1/findRadius(liquid1, 201, 16), 1/findRadius(liquid2, 201, 16), 1/findRadius(liquid3, 201, 16), 1/findRadius(liquid4, 201, 16), 1/findRadius(liquid5, 201, 16)]
inv_rad_error = (1/(radius**2))*rad_error
#getError(1/radius, inv_rad_block)

p_gas_block = [getPressure(gas1), getPressure(gas2), getPressure(gas3), getPressure(gas4), getPressure(gas5)]
p_gas_error = getError(pressure_gas, p_gas_block)

p_liq_block = [getPressure(liquid1), getPressure(liquid2), getPressure(liquid3), getPressure(liquid4), getPressure(liquid5)]
p_liq_error = getError(pressure_liq, p_liq_block)


deltaP_block = []
for i in range (5):
    deltaP_block.append(abs(p_gas_block[i] - p_liq_block[i]))

deltaP = sum(deltaP_block)/5

deltaP_error = getError(deltaP, deltaP_block)



record = open([SURFACE_TENSION_DATA_FILE], "a")
record.write("For drop of initial radius %i: \n" % size)
record.write("The gas pressure is %f, with an error of %f. \n" % (pressure_gas, p_gas_error))
record.write("The liquid pressure is %f, with an error of %f. \n" % (pressure_liq, p_liq_error))
record.write("The droplet radius is %f, with an error of %f. \n" % (radius, rad_error))
record.write("Inverse droplet radius is %f, with an error of %f. \n" % (1/radius, inv_rad_error))
record.write("Finally, deltaP is %f, with an error of %f. \n" % (deltaP, deltaP_error))
record.write("--------\n")