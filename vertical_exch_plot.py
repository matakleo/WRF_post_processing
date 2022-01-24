from netCDF4 import Dataset
from numpy.core.fromnumeric import shape, size, transpose
from wrf import getvar
import numpy as np
import math
import csv
import os
import matplotlib.pyplot as plt

def list_files_8(Dir):
	Post_Processed_Data = []
	for f in os.listdir(Dir):
		Post_Processed_Data.append(f)
	return (Post_Processed_Data)

def list_ncfiles(Dir, ncfiles):
	for f in os.listdir(Dir):
		if f.startswith('wrfout'):
			ncfiles.append(f)
	ncfiles.sort()
	return (ncfiles)

Input_Dir = '/project/momen/Lmatak/WRF/Hurricanes/'
Output_Dir = '/project/momen/Lmatak/WRF/Hurricanes/pblh_data/fixed_hpbls/'
#HNS = ['Iota','Michael','Laura', 'Matthew', 'Maria', 'Dorian', 'Lorenzo', 'Irma']
HNS = ['Dorian', 'Lorenzo', 'Irma']
# Choose between : '32km','8km'
GSS = ['32km']
# Choose between : 'NoTurb','TKE2D'
TMS = ['NoTurb']
# Choose between : 'YSU', 'MYJ', 'ACM2'
PBLS = ['YSU']
# Choose between: '0.25' , '0.5', '1.0' , '2.0' , '4.0' , '8,0'
CLS = ['1.0', 'lvl_2', 'lvl_4', 'lvl_8', 'xkzm_0.25', 'xkzm_4.0']
# spec_name = ['hpbl_0.5','hpbl_fix_400','hpbl_1.0','hpbl_2.0','kpbl_0.5','kpbl_2.0','hpbl_fix_1200','hpbl_fix_800',]
# Identify the time step
Time_Step = 6 
a=0
# Identify the time index
Time_Idx = 0 

# Define all hurricane's settings 
Hurricane_Settings = []
                             
Input_Dir_1 = '/Users/lmatak/Desktop/some_wrfout_files/Doian_latest_8km_hpbl_500'
os.chdir(Input_Dir_1)

ncfiles = []
ncfiles = list_ncfiles (Input_Dir_1, ncfiles)
for ncfile in ncfiles:
    ncfile=Dataset(ncfile)

    U10_2D = np.array(getvar(ncfile, "U10", Time_Idx))
    V10_2D = np.array(getvar(ncfile, "V10", Time_Idx))

    U10_1D = U10_2D.flatten()
    V10_1D = V10_2D.flatten()
    WND_SPD_10 = U10_1D
    # Calculate the wind intensity at each point of the map.
    for i in range (WND_SPD_10.size - 1):
            WND_SPD_10[i] = math.sqrt((U10_1D[i]**2)+(V10_1D[i]**2))
    top_100_idx = np.argsort(WND_SPD_10)[-100:]
    EXCH_M_3D=np.array(getvar(ncfile,"EXCH_M", Time_Idx))
    lvl_heights=[]
    exch=[]
    z=np.array(getvar(ncfile, "z",Time_Idx))
    for i in range(10):
            lvl_heights.append(np.average(z[i].flatten()[top_100_idx]))
            exch.append(np.average(EXCH_M_3D[i].flatten()[top_100_idx]))
            print(np.average(EXCH_M_3D[i].flatten()[top_100_idx]))
    
    plt.plot(exch,lvl_heights)
    plt.show()




