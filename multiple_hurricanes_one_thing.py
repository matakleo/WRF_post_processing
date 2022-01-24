from numpy.core.function_base import linspace
from Func_Extract_Data import Extract_the_shit,Extract_Coordinates_2,Extract_Track_Data,flatten_the_curve
import cartopy.feature as cfeature
import matplotlib.gridspec as gridspec
#from Func_Map_Setting import map_setting
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Input_Dir = '/Users/lmatak/Desktop/leo_simulations/WRF_Output_PBLHS/diff_hpbls'

HNS = ['Dorian','Iota','Lorenzo','Laura']
GSS = ['4km']
TMS= ['NoTurb']
PBLS = ['YSU']
CLS = ['1.0','250','2000']
i=0
Time_idx = '0'
Times = [0,6, 12, 18, 24, 30, 36, 42, 48,54,60,66,72,80]
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(12,8), sharey='row', sharex='col')
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.05, hspace=0.05)
colors=['red','blue','lightblue']
format="linewidth='2',color=colors[c],label='HBL - '+CL"
for HN in HNS:
    c=0 #color counter
    i+=1
    for GS in GSS:
        for TM in TMS:
            for PBL in PBLS:
                for CL in CLS:
                    Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'
                    #real data 
                    Real_slp=[]
                    Real_slp = Extract_the_shit(Real_Hurricane_Data,Real_slp,'Pressure (mb) ')
                    Real_Winds=[]
                    Real_Winds = Extract_the_shit(Real_Hurricane_Data,Real_Winds,'Wind Speed(kt)')


                    Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
                    Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'
                    csv_file = (Input_Dir_1+Hurricane_Setting)


                    min_slp_simulation=[]
                    min_slp_simulation = Extract_the_shit (csv_file, min_slp_simulation, 'min_slp')
                    Wind_Speed = []
                    Wind_Speed_simulation = Extract_the_shit (csv_file, Wind_Speed, 'All_Max_WND_SPD_10')

                    #upper row ploting
                    plt.subplot(2,4,i) 
                    plt.plot(Times[:len(Real_Winds)],Real_Winds,linewidth='2',color='black')
                    plt.plot(Times[:len(Wind_Speed_simulation)],Wind_Speed_simulation,color=colors[c],linewidth='2')
                    plt.title(HNS[i-1])
                    
                    #lower row plotting
                    plt.subplot(2,4,len(HNS)+i) 
                    plt.plot(Times[:len(Real_slp)],Real_slp,label='Real Data',linewidth='2',color='black')
                    plt.plot(Times[:len(min_slp_simulation)],min_slp_simulation,linewidth='2',color=colors[c],label=CL)
                    plt.xticks(Times[:len(min_slp_simulation)])
                    plt.xlabel('Time [hr]')
                    c+=1    #color counter

#adding y axis labels
plt.subplot(2,4,1)
plt.ylabel('Wind Intensity [m/s]')
plt.subplot(2,4,5)
plt.ylabel('Min SLP [hPa]')
#add the title
fig.suptitle('Time series of wind intensity and SLP')
handles, labels = fig.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
fig.legend(by_label.values(), by_label.keys(), loc = 'upper center', mode='expand',
			 ncol = 4, bbox_to_anchor=(0.65, 0.96, -0.3, 0),frameon = False)
plt.show()