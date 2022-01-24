from numpy.core.function_base import linspace
from numpy.lib.function_base import extract
from Func_Extract_Data import Extract_by_name,Extract_Coordinates_2,Extract_Track_Data,flatten_the_curve
import cartopy.feature as cfeature
import matplotlib.gridspec as gridspec
#from Func_Map_Setting import map_setting
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'
Input_Dir = '/Users/lmatak/Desktop/leo_simulations/WRF_Output_PBLHS/diff_hpbls'
# for MYJ 'Maria','Dorian','Irma','Laura'
HNS = ['Laura']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['8km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TMS = ['NoTurb']
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBLS = ['YSU']

CLS = ['1.0','lvl_2','lvl_4','lvl_8']#,'250','2000']
CLS_myj=['1.0','kh_0.25','kh_4.0','250','2000']



Time_idx = '0'


# fig.tight_layout()


fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(14,8), sharey='row')#, sharex='col')
# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.05, hspace=0.05)



colors = ['blue', 'orange', 'red', 'green', 'purple', 'magenta','yellow']
line_stylez= ['-','--','-.']
c=0
i=0



Times = [0,6, 12, 18, 24, 30, 36, 42, 48,54,60,66,72,80]

for HN in HNS:
    c=0 #color counter

    for GS in GSS:
        for TM in TMS:
            for PBL in PBLS:
                i+=1
                counter_pbls=0
                for CL in CLS:
                    Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/Standard/'
                    print('Input dir: ',Input_Dir_1)
                    #by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
                    Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'
                    csv_file = (Input_Dir_1+Hurricane_Setting)
                    print(csv_file)
                    lvl_heights=[]
                    lvl_heights = Extract_by_name(csv_file, lvl_heights, 'lvl_heights')
                    exch_m=[]
                    exch_h=[]
                    ratio_of_coefficients=[]
                    if PBL == 'MYJ':
                        exch_m=Extract_by_name(csv_file,exch_m,'avg_vert_exch_akmkl')
                    # print(exch_m)
                        exch_h=Extract_by_name(csv_file,exch_h,'avg_vert_exch')
                    else:
                        exch_m=Extract_by_name(csv_file,exch_m,'avg_vert_exch_momentum')
                        # print(exch_m)
                        exch_h=Extract_by_name(csv_file,exch_h,'avg_vert_exch_scalar')
                    for j in range(len(exch_m)):
                        try:
                            ratio_of_coefficients.append(exch_h[j]/exch_m[j])
                        except: ratio_of_coefficients.append(0)
                    plt.subplot(2,4,i) 
                    if PBL == 'MYJ':
                        plt.plot(ratio_of_coefficients, lvl_heights, color=colors[c], linestyle='-', marker='.', 
                        linewidth='3',markersize='7',  label= (PBL+'-'+CLS_myj[counter_pbls]))
                    else:
                        plt.plot(ratio_of_coefficients, lvl_heights, color=colors[c], linestyle='-', marker='.', 
                        linewidth='3',markersize='7',  label= (PBL+'-'+CLS[counter_pbls]))

                    plt.title(HNS[i-1])

                    # plt.subplot(2,4,) 
                    # plt.plot(ratio_of_coefficients, lvl_heights, color=colors[c], linestyle='-', marker='.', 
                    # linewidth='3',markersize='7',  label= (PBL+'-'+CLS[counter_pbls]))
                    # plt.title(HNS[i-1])

                    counter_pbls+=1
                    c+=1
fig.suptitle('Kh/Km coefficient ratio vertical profiles')
handles, labels = fig.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
fig.legend(by_label.values(), by_label.keys(), loc = 'upper center', mode='expand',
			 ncol = 5, bbox_to_anchor=(0.75, 0.96, -0.5, 0),frameon = False)
plt.show()
 
                

            