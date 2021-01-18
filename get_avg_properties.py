from getError import getError
from getAvgPotPerVol import getAvgs
from oneBigFile import oneBigFile
import os.path
from os import path

size = [INITIAL RAD]
limit = 45

end_liquid_potener = [FULL LIQUID POTENTIAL ENERGY FILE]
end_gas_potener = [FULL VAPOR POTENTIAL ENERGY FILE]
end_surface_potener = [FULL SURFACE POTENTIAL ENERGY FILE]

end_liquid_density = [FULL LIQUID DENSITY FILE]
end_gas_density = [FULL VAPOR DENSITY FILE]
end_surface_density = [FULL SURFACE DENSITY FILE]

liquid_pot1 = [LIQUID_POTENTIAL_ENERGY_FILE_1]
liquid_pot2 = [LIQUID_POTENTIAL_ENERGY_FILE_2]
liquid_pot3 = [LIQUID_POTENTIAL_ENERGY_FILE_3]
liquid_pot4 = [LIQUID_POTENTIAL_ENERGY_FILE_4]
liquid_pot5 = [LIQUID_POTENTIAL_ENERGY_FILE_5]

if not path.exists(end_liquid_potener):
    oneBigFile(end_liquid_potener, liquid_pot1, liquid_pot2, liquid_pot3, liquid_pot4, liquid_pot5)

gas_pot1 = [VAPOR_POTENTIAL_ENERGY_FILE_1]
gas_pot2 = [VAPOR_POTENTIAL_ENERGY_FILE_2]
gas_pot3 = [VAPOR_POTENTIAL_ENERGY_FILE_3]
gas_pot4 = [VAPOR_POTENTIAL_ENERGY_FILE_4]
gas_pot5 = [VAPOR_POTENTIAL_ENERGY_FILE_5]

if not path.exists(end_gas_potener):
    oneBigFile(end_gas_potener, gas_pot1, gas_pot2, gas_pot3, gas_pot4, gas_pot5)

surf_pot1 = [SURFACE_POTENTIAL_ENERGY_FILE_1]
surf_pot2 = [SURFACE_POTENTIAL_ENERGY_FILE_2]
surf_pot3 = [SURFACE_POTENTIAL_ENERGY_FILE_3]
surf_pot4 = [SURFACE_POTENTIAL_ENERGY_FILE_4]
surf_pot5 = [SURFACE_POTENTIAL_ENERGY_FILE_5]

if not path.exists(end_surface_potener):
    oneBigFile(end_surface_potener, surf_pot1, surf_pot2, surf_pot3, surf_pot4, surf_pot5)

liquid_dens1 = [LIQUID_DENSITY_FILE_1]
liquid_dens2 = [LIQUID_DENSITY_FILE_2]
liquid_dens3 = [LIQUID_DENSITY_FILE_3]
liquid_dens4 = [LIQUID_DENSITY_FILE_4]
liquid_dens5 = [LIQUID_DENSITY_FILE_5]

if not path.exists(end_liquid_density):
    oneBigFile(end_liquid_density, liquid_dens1, liquid_dens2, liquid_dens3, liquid_dens4, liquid_dens5)

gas_dens1 = [VAPOR_DENSITY_FILE_1]
gas_dens2 = [VAPOR_DENSITY_FILE_2]
gas_dens3 = [VAPOR_DENSITY_FILE_3]
gas_dens4 = [VAPOR_DENSITY_FILE_4]
gas_dens5 = [VAPOR_DENSITY_FILE_5]

if not path.exists(end_gas_density):
    oneBigFile(end_gas_density, gas_dens1, gas_dens2, gas_dens3, gas_dens4, gas_dens5)

surf_dens1 = [SURFACE_DENSITY_FILE_1]
surf_dens2 = [SURFACE_DENSITY_FILE_2]
surf_dens3 = [SURFACE_DENSITY_FILE_3]
surf_dens4 = [SURFACE_DENSITY_FILE_4]
surf_dens5 = [SURFACE_DENSITY_FILE_5]

if not path.exists(end_surface_density):
    oneBigFile(end_surface_density, surf_dens1, surf_dens2, surf_dens3, surf_dens4, surf_dens5)

avg_gas_density, avg_gas_potener = getAvgs(end_gas_potener, end_gas_density)
avg_liq_density, avg_liq_potener = getAvgs(end_liquid_potener, end_liquid_density)
avg_surf_density, avg_surf_potener = getAvgs(end_surface_potener, end_surface_density)


avg_gd_1, avg_gp_1 = getAvgs(gas_pot1, gas_dens1)
avg_gd_2, avg_gp_2 = getAvgs(gas_pot2, gas_dens2)
avg_gd_3, avg_gp_3 = getAvgs(gas_pot3, gas_dens3)
avg_gd_4, avg_gp_4 = getAvgs(gas_pot4, gas_dens4)
avg_gd_5, avg_gp_5 = getAvgs(gas_pot5, gas_dens5)

avg_ld_1, avg_lp_1 = getAvgs(liquid_pot1, liquid_dens1)
avg_ld_2, avg_lp_2 = getAvgs(liquid_pot2, liquid_dens2)
avg_ld_3, avg_lp_3 = getAvgs(liquid_pot3, liquid_dens3)
avg_ld_4, avg_lp_4 = getAvgs(liquid_pot4, liquid_dens4)
avg_ld_5, avg_lp_5 = getAvgs(liquid_pot5, liquid_dens5)

avg_sd_1, avg_sp_1 = getAvgs(surf_pot1, surf_dens1)
avg_sd_2, avg_sp_2 = getAvgs(surf_pot2, surf_dens2)
avg_sd_3, avg_sp_3 = getAvgs(surf_pot3, surf_dens3)
avg_sd_4, avg_sp_4 = getAvgs(surf_pot4, surf_dens4)
avg_sd_5, avg_sp_5 = getAvgs(surf_pot5, surf_dens5)

gas_dens_error = getError(avg_gas_density, [avg_gd_1, avg_gd_2, avg_gd_3, avg_gd_4, avg_gd_5])
gas_pot_error = getError(avg_gas_potener, [avg_gp_1, avg_gp_2, avg_gp_3, avg_gp_4, avg_gp_5])

liq_dens_error = getError(avg_liq_density, [avg_ld_1, avg_ld_2, avg_ld_3, avg_ld_4, avg_ld_5])
liq_pot_error = getError(avg_liq_potener, [avg_lp_1, avg_lp_2, avg_lp_3, avg_lp_4, avg_lp_5])

surf_dens_error = getError(avg_surf_density, [avg_sd_1, avg_sd_2, avg_sd_3, avg_sd_4, avg_sd_5])
surf_pot_error = getError(avg_surf_potener, [avg_sp_1, avg_sp_2, avg_sp_3, avg_sp_4, avg_sp_5])

record = open([DATA INFO TEXT FILE], "a")
record.write("For [SYSTEM]:\n")
record.write("Average liquid potener/volume is %f, with error %f.\n" % (avg_liq_potener, liq_pot_error))
record.write("Average surface potener/volume is %f, with error %f.\n" % (avg_surf_potener, surf_pot_error))
record.write("Average gas potener/volume is %f, with error %f.\n" % (avg_gas_potener, gas_pot_error))
record.write("Average liquid density is %f, with error %f.\n" % (avg_liq_density, liq_dens_error))
record.write("Average surface density is %f, with error %f.\n" % (avg_surf_density, surf_dens_error))
record.write("Average gas density is %f, with error %f.\n" % (avg_gas_density, gas_dens_error))
record.write("---------\n")