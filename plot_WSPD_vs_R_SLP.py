from numpy.core.function_base import linspace
from Func_Extract_Data import Extract_the_shit2,Extract_Coordinates_2,Extract_Track_Data,flatten_the_curve
import cartopy.feature as cfeature
import matplotlib.gridspec as gridspec
#from Func_Map_Setting import map_setting
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs






Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

Input_Dir = '/Users/lmatak/Desktop/leo_simulations/WRF_Output_PBLHS/diff_hpbls'
# Choose between : 'Dorian','Iota','Irma','Laura','Lorenzo','Maria','Matthew','Michael'
# for MYJ 'Maria','Dorian','Irma','Laura'
HN = 'Iota'
# Choose between : '2km', '4km', '8km', '16km', '32km'
GS = '4km'
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TM = 'NoTurb'
# Choose between : 'YSU_wrf_42',YSU_lin_63'
PBLS = ['YSU']

CLS = ['1.0','xkzm_0.25','xkzm_4.0']



Time_idx = '6'
PBL_counter=0
fig = plt.figure(figsize=(18, 9))
fig.tight_layout()


gs = gridspec.GridSpec(1,2,figure=fig,wspace=0.3,hspace=0.6)
#normaln ones
ax1 = fig.add_subplot(gs[:,:1])
ax2 =fig.add_subplot(gs[:,1:])

colors = ['darkblue', 'darkgreen','darkred' ,'lightgreen', 'magenta','yellow']
line_stylez= ['-','--','-.']
c=0

Input_Dir_1 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/' + 'WSPD_R/'
Input_Dir_2 = Input_Dir + '/' + HN + '/' + GS + '/' + TM + '/' + 'WSPD_SLP/'
# os.chdir(Input_Dir_1)
print('Input dir: ',Input_Dir_1)

Times = [0,6, 12, 18, 24, 30, 36, 42, 48,54,60,66,72,80]


os.chdir(Real_data_dir)
Real_Hurricane_Data = Real_data_dir+'/Real_Data_'+HN+'.csv'


for PBL in PBLS:
	cls_counter=0
	for CL in CLS:

		#by hurricane setting you define the name of the csv file e.g. /Irma_32km_NoTurb_YSU_hpbl_250.csv/
		Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL +'.csv'		
		# print(Hurricane_Setting)
		csv_file1 = (Input_Dir_1+Hurricane_Setting)
		csv_file2 = (Input_Dir_2+Hurricane_Setting)
		print(csv_file1)

		Radiuses=[]
		Radiuses = Extract_the_shit2(csv_file1, Radiuses, 'Radiuses')
		Average_WSPD=[]
		Average_WSPD= Extract_the_shit2(csv_file1,Average_WSPD,' Average_WSPD')

		SLPS=[]
		SLPS=Extract_the_shit2(csv_file2, SLPS, 'SLPS')
		avg_wspds_slp=[]
		avg_wspds_slp=Extract_the_shit2(csv_file2, avg_wspds_slp, ' Average_WSPD')
		 
# 		#you define empty lists which will contain the extracted data from the csv file, and plot them immediatle


		ax1.plot(Radiuses, Average_WSPD, color=colors[c], linestyle=line_stylez[PBL_counter], marker='.', 
			linewidth='1.5',markersize='7',label= (PBL+'-'+CLS[cls_counter]))
		ax1.set_title('WSPD vs R')

		ax2.plot(SLPS,avg_wspds_slp,color=colors[c], linestyle=line_stylez[PBL_counter], marker='.', 
			linewidth='1.5',markersize='7',label= (PBL+'-'+CLS[cls_counter]))
		ax2.set_title('WSPD vs SLP')

		


		cls_counter+=1
		c+=1
	PBL_counter+=1


handles, labels = fig.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
# ax2.set_xticks(xticks)
# ax3.set_xticks(xticks)

# plt.legend()
fig.legend(by_label.values(), by_label.keys(), loc = 'upper center', mode='expand',
			 ncol = 3, bbox_to_anchor=(0.65, 0.96, -0.3, 0),frameon = False)
fig.suptitle(HN+' - '+GS+' - '+TM+' - '+PBL, fontsize=18)
plt.show()