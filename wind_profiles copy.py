from Func_List_Files import  (list_hurricane_settings, list_csv_files_3)
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.gridspec as gridspec
from Func_Extract_Data import Extract_the_shit2
import matplotlib.pyplot as plt
import numpy as np
import os

# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "sans-serif",
#     "font.sans-serif": ["Helvetica"]})
# # for Palatino and other serif fonts use:
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.serif": ["Palatino"],
# })
fig = plt.figure(figsize=(16, 6),)

gs = gridspec.GridSpec(1,5,figure=fig,wspace=0)
ax1 =fig.add_subplot(gs[0],)
ax2 =fig.add_subplot(gs[1])

ax3 =fig.add_subplot(gs[3])
ax4 =fig.add_subplot(gs[4])

plt.setp(ax2.get_yticklabels(), visible=False)

plt.setp(ax4.get_yticklabels(), visible=False)

axess = [ax1,ax2,ax3,ax4]
print(gs)
print('YAY')



loop_counter = 0
# List the colors that will be used for tracing the wind intensity.
colors = ['red', 'green', 'purple', 'blue', 'black']
figure_indices = np.array([['(a)', '(b)', '(c)', '(d)', '(e)', '(f)'],
					['(g)', '(h)', '(i)', '(j)', '(k)', '(l)']])
Input_Dir = '/Users/lmatak/Desktop/leo_simulations/WRF_Output_PBLHS/diff_hpbls'
# Choose between : 'Gustav', 'Irma', 'Katrina', 'Maria'
HNS = ['Lorenzo']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['4km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D's
TMS = [ 'NoTurb']
# Choose between : 'cl_0.25' , 'cl_0.5' , 'cl_1.0' , 'cl_2.0' ,'cl_4.0'
PBLS = ['YSU']
CLS = ['1.0' , 'xkzm_0.25' , 'xkzm_4.0']
# Define all hurricane's settings 
# Define all hurricane's settings 
Hurricane_Settings = []
c = 0

for HN in HNS:
	for GS in GSS:
		count_TM = 0
		for TM in TMS:
			for PBL in PBLS:
				for CL in CLS:
					#print('LOOOOOP COUNT = ' ,loop_counter)
					l=0
			
					# This list will contain all the csv_files containing the data for different times.
					csv_files = []
					Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_REY_hpbl_'+CL	
					print (Hurricane_Setting)
					Hurricane_Settings.append(Hurricane_Setting)
					Input_Dir_2 = Input_Dir + '/' + HN + '/' + GS + '/'+TM+'/Reynolds/' + Hurricane_Setting
					print (Input_Dir_2)
					list_csv_files_3 (Input_Dir_2, csv_files)
					count_VR = 0
					
					for csv_file in csv_files[-2:] :
						print(csv_file)
						os.chdir(Input_Dir_2)
						
	# 					#print (csv_file)
						#Define  the lists that will contain the data.
						sp_tm_avg_ur    = []
						sp_tm_avg_uth   = []
						sp_tm_avg_uz    = []
						sp_tm_avg_uruth = []
						sp_tm_avg_uruz  = []
						sp_tm_avg_uthuz = []

						sp_avg_Trtth    = []
						sp_avg_Trtz     = []
						sp_avg_Tthtz    = []

						sp_tm_avg_mrmth = []
						sp_tm_avg_mrmz  = []
						sp_tm_avg_mthmz = []
						
						Rey_uruth       = []
						Rey_uruz        = []
						Rey_uthuz       = []
						z               = []
						# This list will contain all the altitudes below 5000 m.row_header.index(Variable_Name)
						z_5000          = []

						# Extract the necessary data.
						sp_tm_avg_ur= Extract_the_shit2(csv_file,sp_tm_avg_ur,'sp_tm_avg_ur')
						sp_tm_avg_uth=Extract_the_shit2 (csv_file, sp_tm_avg_uth, 'sp_tm_avg_uth')
						sp_tm_avg_uz=Extract_the_shit2 (csv_file, sp_tm_avg_uz, 'sp_tm_avg_uz')					
						sp_tm_avg_uruth=Extract_the_shit2 (csv_file, sp_tm_avg_uruth, 'sp_tm_avg_uruth')
						sp_tm_avg_uruz=Extract_the_shit2 (csv_file, sp_tm_avg_uruz, 'sp_tm_avg_uruz')
						sp_tm_avg_uthuz=Extract_the_shit2 (csv_file, sp_tm_avg_uthuz, 'sp_tm_avg_uthuz')

						sp_avg_Trtth=Extract_the_shit2 (csv_file, sp_avg_Trtth, 'sp_avg_Trth')
						sp_avg_Trtz=Extract_the_shit2 (csv_file, sp_avg_Trtz, 'sp_avg_Trz')
						sp_avg_Tthtz=Extract_the_shit2 (csv_file, sp_avg_Tthtz, 'sp_avg_Tthz')

						sp_tm_avg_mrmth=Extract_the_shit2 (csv_file, sp_tm_avg_mrmth, 'sp_tm_avg_mrth')
						sp_tm_avg_mrmz=Extract_the_shit2 (csv_file, sp_tm_avg_mrmz, 'sp_tm_avg_mrz')
						sp_tm_avg_mthmz=Extract_the_shit2 (csv_file, sp_tm_avg_mthmz, 'sp_tm_avg_mthz')


						z=Extract_the_shit2(csv_file, z, 'z')

						# Calculate Reynolds stresses.
						for n in range (len (z)):
						
							if z[n]<= 5000:
								Rey_uruth.append(sp_tm_avg_uruth[n] - (sp_tm_avg_ur[n] * sp_tm_avg_uth[n]) + sp_avg_Trtth[n] + sp_tm_avg_mrmth[n])
								Rey_uruz.append(sp_tm_avg_uruz[n] - (sp_tm_avg_ur[n] * sp_tm_avg_uz[n]) + sp_avg_Trtz[n] + sp_tm_avg_mrmz[n])
								Rey_uthuz.append(sp_tm_avg_uthuz[n] - (sp_tm_avg_uth[n] * sp_tm_avg_uz[n]) + sp_avg_Tthtz[n] + sp_tm_avg_mthmz[n])
								z_5000.append(z[n]/1000)
						print ('Rey_uruth length' ,len(Rey_uruth))
						print ('Rey_uruz' ,len(Rey_uruz))
						print ('Rey_uthuz' ,len(Rey_uthuz))
						print (len(z_5000))
						
	# 					# Plot Reynolds stresses.
						print('l=',l)
						print('l+3 =',l+3)
						axess[l].plot(sp_tm_avg_ur[0:len(z_5000)], z_5000, color=colors[c], linewidth=2, label = 'hpbl - '+CL)
						axess[l+1].plot(sp_tm_avg_uth[0:len(z_5000)], z_5000, color=colors[c], linewidth=2, label = 'hpbl - '+CL)
						# axess[l+2].plot(Rey_uthuz, z_5000, color=colors[c], linewidth=2, label = CLH)
						
						
			
						# Set x_axis and y_axis labels.
						axess[l].set_ylabel("z [km]", fontsize=10)
						axess[l].set_xlabel('ur')
						axess[l+1].set_xlabel('utheta')
						
						# axess[l].set_xlabel(r"$\overline{u'_ru'_{\theta}}$" + " [m" + r"$^2$" + "/s" + r"$^2$" + "]", fontsize=10)
						# axess[l+1].set_xlabel(r"$\overline{u'_ru'_z}$" + " [m" + r"$^2$" + "/s" + r"$^2$" + "]", fontsize=10)
						# axess[l+2].set_xlabel(r"$\overline{u'_{\theta}u'_z}$" + " [m" + r"$^2$" + "/s" + r"$^2$" + "]", fontsize=10)


						# Write SLP pressure intervals.
						
						

						# te simulation's caracteristics.
						axess[l].set_title(HN[0:3] + '-' + GS + '-' + TM, {'size': 10}, pad= -1, y = 0.97)
						axess[l+1].set_title(HN[0:3] + '-' + GS + '-' + TM, {'size': 10}, pad= -1, y = 0.97)
						# axess[l+2].set_title(HN[0:3] + '-' + GS + '-' + TM, {'size': 10}, pad= -1, y = 0.97)


						

						l=l+2
					c=c+1


text_1 = "0.995 " + r'$\leq$' + " " + r'$\frac{SLP}{SLP_{MW}}$' + r'$\leq$' + " " + "1"
text_2 = "1.005 " + r'$\leq$' + " " + r'$\frac{SLP}{SLP_{MW}}$' + r'$\leq$' + " " + "1.0075"

axess[0].annotate(text_1, xy=(0.9, 1), xytext=(0, 350), textcoords='axes points',
					color='black', size='medium')
axess[-1].annotate(text_2, xy=(0.9, 1), xytext=(30, 350), textcoords='axes points',
color='black', size='medium')
					
				
# 					count_VR = 3	
# 					gs = gs01
				
# 			count_TM = count_TM + 1
# 			c = c + 1 

handles, labels = fig.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
fig.legend(by_label.values(), by_label.keys(), loc = 'upper center', mode='expand',
			 ncol = 5, bbox_to_anchor=(0.6, 0.955, -0.2, 0),frameon = False)
# fig.legend(labels=['cL = 0.25', 'cL = 0.5', 'cL = 1.0', 
# 	'cL = 2.0'], bbox_to_anchor=(0.6, 0.955, -0.2, 0), loc = 'upper center', frameon = False,
#  	mode='expand', ncol = 4)	
fig.suptitle(HN+' - '+GS+' - '+TM+' - '+PBL, fontsize=18)
plt.show()
