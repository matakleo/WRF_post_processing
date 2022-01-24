from Func_Extract_Data import Extract_the_shit,Extract_Coordinates_2,Extract_Track_Data,flatten_the_curve
from Func_List_Files import list_csv_files_0
from wrf import (get_cartopy,cartopy_xlim, cartopy_ylim, latlon_coords)
import cartopy.feature as cfeature
from cartopy.feature import NaturalEarthFeature
import matplotlib.gridspec as gridspec
#from Func_Map_Setting import map_setting
import os
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from Func_Error import calculate_distance_error,calculate_intensity_error

Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'
os.chdir(Real_data_dir)
Input_Dir = '/Users/lmatak/Desktop/leo_simulations/WRF_Output_PBLHS/diff_hpbls'
# Choose between : 'Dorian','Laura','Lorenzo','Maria','Irma','Iota'
HNS = ['Dorian','Laura','Lorenzo','Maria','Irma','Iota']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '8km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBLS = ['YSU']
# Choose between: '0.25', '0.5', '1.0', '2.0' ,'4.0'
CLS = ['1.0','xkzm_0.25','xkzm_4.0']
# colors = ['blue', 'orange', 'red', 'green', 'purple', 'magenta','yellow']
colors = ['red', 'green', 'purple', 'magenta','yellow','blue']
fig = plt.figure(figsize=(8, 8), constrained_layout=True)
gs = gridspec.GridSpec(1,3,figure=fig,wspace=0.2)
all_hurs_track_error_list=[]
all_hurs_wind_intensity_error_list=[]
all_hurs_min_slp_error_list=[]
List_Of_Hurricanes=[]
Average_List_Of_Hurricanes=[]
List_for_CSV_files=[]
Time_Idx = 0
ax1 = fig.add_subplot(gs[0,0])
ax2 =fig.add_subplot(gs[0,1])
ax3 =fig.add_subplot(gs[0,2])
axxess=(ax1,ax2,ax3)
for PBL in PBLS:
    for CL in CLS:
        List_Of_Hurricanes.append('Error_all_hurricanes_'+PBL+'_hpbl_'+CL)
        Average_List_Of_Hurricanes.append('Average_Error_List_'+PBL+'_hpbl_'+CL)
        List_for_CSV_files.append(PBL+'_hpbl_'+CL)

for HN in HNS:

    Hurricane_Dir =Input_Dir + '/' + HN + '/' + GS + '/' + TM +'/'  
    Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'

    Real_Lats = []
    Real_Longs = []
    Real_Lats = Extract_Track_Data (Real_data_dir, Real_Lats, 'Lat',HN)
    Real_Longs = Extract_Track_Data (Real_data_dir, Real_Longs, 'Lon',HN)

    Real_slp=[]
    Real_slp = Extract_the_shit(Real_Hurricane_Data,Real_slp,'Pressure (mb) ')

    Real_Winds=[]
    Real_Winds = Extract_the_shit(Real_Hurricane_Data,Real_Winds,'Wind Speed(kt)')

    csv_files=list_csv_files_0(Hurricane_Dir,List_for_CSV_files)
    print(csv_files)

    
    error_list_track=[]
    error_list_wind_intensity=[]
    error_list_min_slp=[]
    for csv_file in csv_files:

        Eye_Lats=[]
        Eye_Longs=[]
        simulated_wind_intensities=[]
        simulated_min_slp=[]

        Eye_Lats=Extract_the_shit(csv_file,Eye_Lats,'min_lat')
        Eye_Longs=Extract_the_shit(csv_file,Eye_Longs,'min_long')
        simulated_wind_intensities=Extract_the_shit(csv_file,simulated_wind_intensities,'All_Max_WND_SPD_10')
        simulated_min_slp=Extract_the_shit(csv_file,simulated_min_slp,'min_slp')
        number = (int((len(Eye_Lats)-1)/(len(Real_Lats)-1)))
        if number == 0:
            number =1
        print(number)
        Eye_Lats2=[]
        Eye_Longs2=[]
        simulated_wind_intensities2=[]
        simulated_min_slp2=[]
        for i in range(len(Eye_Lats)):


            Eye_Lats2.append(Eye_Lats[i*number])
            Eye_Longs2.append(Eye_Longs[i*number])
            simulated_wind_intensities2.append(simulated_wind_intensities[i*number])
            simulated_min_slp2.append(simulated_min_slp[i*number])


        print(Eye_Lats2)
        error_list_track.append(calculate_distance_error(Eye_Lats2, Eye_Longs2, Real_Lats[0:len(Eye_Lats2)], Real_Longs[0:len(Eye_Lats2)]))
        print(error_list_track)
        error_list_wind_intensity.append(calculate_intensity_error(simulated_wind_intensities2,Real_Winds))
        error_list_min_slp.append(calculate_intensity_error(simulated_min_slp2,Real_slp))

    all_hurs_track_error_list.append(error_list_track)
    print(all_hurs_track_error_list)
    all_hurs_wind_intensity_error_list.append(error_list_wind_intensity)
    all_hurs_min_slp_error_list.append(error_list_min_slp)

all_hurs_min_slp_error_list=np.array(all_hurs_min_slp_error_list)       
all_hurs_wind_intensity_error_list=np.array(all_hurs_wind_intensity_error_list)
all_hurs_track_error_list=np.array(all_hurs_track_error_list)
avg_track=[]
avg_wind=[]
avg_slp=[]

for i in range(len(CLS)):
    avg_track.append(np.average(all_hurs_track_error_list[:,i]))
    avg_wind.append(np.average(all_hurs_wind_intensity_error_list[:,i]))
    avg_slp.append(np.average(all_hurs_min_slp_error_list[:,i]))
x_ticks=(0,1,2,3,4,5,6,7,8,9)

for i in range(len(CLS)):
    ax1.bar(i,avg_track[i],label= (PBL+'-'+CLS[i]), color=colors[i])
    ax2.bar(i,avg_wind[i],label= (PBL+'-'+CLS[i]), color=colors[i])
    ax3.bar(i,avg_slp[i],label= (PBL+'-'+CLS[i]), color=colors[i])
ax1.set_xticks(x_ticks[0:len(CLS)])
ax1.set_title('Track error')
ax1.set_ylabel('[km]')

ax2.set_xticks(x_ticks[0:len(CLS)])
ax2.set_title('Wind intensity error')
ax2.set_ylabel('%')

ax3.set_xticks(x_ticks[0:len(CLS)])
ax3.set_title('Min slp error')
ax3.set_ylabel('%')

ax1.set_xticklabels(CLS)
ax2.set_xticklabels(CLS)
ax3.set_xticklabels(CLS)
ax1.set_xlabel('hpbl [m]', fontsize=12)
ax2.set_xlabel('hpbl [m]', fontsize=12)
ax3.set_xlabel('hpbl [m]', fontsize=12)
fig.suptitle(', '.join(HNS)+' - '+PBL+' - '+GS, fontsize=16)
for i in axxess:
    print(i)




# ax.set_ylabel('Error Track (km)', fontsize=12)
# ax.set_xlabel('CLS', fontsize=12)
# #ax.set_xticks(x_pos)
# ax.set_xticks(x_ticks)
# ax.set_xticklabels(CLSx)
# #ax[0].legend()
# #ax[0].set_title('The average error of all hurricane versus the grid size for each turbulent model')
# ax.yaxis.grid(True)
plt.show()



