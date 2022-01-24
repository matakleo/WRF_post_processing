
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

###############################################################################################
# This function checks if a file name exists in the output directory otherwise it creates it. #
###############################################################################################

def create_file (Output_Dir, File_name):
	
	os.chdir(Output_Dir)
	files = []
	files = list_files_8 (Output_Dir)
	test = False
	for file in files:
		if file == File_name:
			test = True
			break
	if test == False:
		os.mkdir (File_name)
	os.chdir (Output_Dir + File_name)

#check the output folder!!!!

Input_Dir = '/Users/lmatak/Desktop/some_wrfout_files/'

Output_Dir = '/Users/lmatak/Desktop/some_wrfout_files/output_files/'
#HNS = ['Iota','Michael','Laura', 'Matthew', 'Maria', 'Dorian', 'Lorenzo', 'Irma']
HNS = ['Iota']
# Choose between : '32km','8km'
GSS = ['8km']
# Choose between : 'NoTurb','TKE2D'
TMS = ['NoTurb']
# Choose between : 'YSU', 'MYJ', 'ACM2'
PBLS = ['ACM2']
# Choose between: '0.25' , '0.5', '1.0' , '2.0' , '4.0' , '8,0'
CLS = ['1.0']
# spec_name = ['hpbl_0.5','hpbl_fix_400','hpbl_1.0','hpbl_2.0','kpbl_0.5','kpbl_2.0','hpbl_fix_1200','hpbl_fix_800',]
# Identify the time step
Time_Step = 6 
a=0
# Identify the time index
Time_Idx = 3

# Define all hurricane's settings 
Hurricane_Settings = []

for HN in HNS:
        counter_for_mid_pbl=0
        for GS in GSS:
                for TM in TMS:
                        for PBL in PBLS:
                                for CL in CLS:

                                        Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL + '_hpbl_' + CL
                             
                                       

                                        # Input_Dir_1 = Input_Dir + HN + '/' + GS + '/HPBL_SENSITIVITY/'  + PBL +'/'+ TM + '/'+ Hurricane_Setting
                                       
                                        ##THIS FOLDER WORKS FOR LOCAL!$$
                                        ################################
                                        Input_Dir_1 = Input_Dir + Hurricane_Setting
                                        print(Input_Dir_1)

                                        # Input_Dir_1 = '/Users/lmatak/Desktop/Lorenzo_Sims/Dorian_4km_hpbl_2000'
                                        # This list will contain all the csv_files containing the data for different times.
                                        csv_files = []
                                        os.chdir(Input_Dir_1)
                                        #Input_Dir = '/project/momen/Lmatak/WRF/Hurricanes/' + HN+'/32km/YSU_HPBL/'
                                  
                                        ncfiles = []
                                        ncfiles = list_ncfiles (Input_Dir_1, ncfiles)

                                        vert_exch_vert_prof=[]
                                        lvl_heights=[]
                                        
                                        #print (Ending_Date)
                                        #list of pblh lvls
                                        average_kpbls=[]
                                        #list for actual heights [m]
                                        average_PBLHS=[]
                                        #list for wspsds
                                        All_Max_WND_SPD_10=[]
                                        #list for vertical exchange coefficients
                                        average_exch_lvl_0=[]
                                        average_exch_lvl_1=[]
                                        average_exch_lvl_2=[]
                                        average_exch_lvl_3=[]
                                        average_exch_lvl_4=[]
                                        average_exch_lvl_5=[]
                                        average_exch_lvl_6=[]
                                        average_exch_lvl_7=[]
                                        average_exch_ms=[]
                                        exch_m=[]
                                        exch_m_mid_pbl=[]
                                        average_exch_ms_mid_pbl=[]
                                        average_mid_lvl_pbl =[]
                                        # initiate the list that will contain the hurricane-track data
                                        min_slp = []
                                        min_lat = []
                                        min_long = []

                                        ### vor vertical lvl heights
                                        z=[]
                                        ncfile_counter=0
                                        print(int(len(ncfiles)/2))
                                        z_file = Dataset(ncfiles[int(len(ncfiles)/2)])
                                        z=np.array(getvar(z_file, "z",Time_Idx))
                                        for ncfile in ncfiles:
                                                ncfile_counter+=1

                                                #print (ncfile)
                                                ncfile = Dataset(ncfile)
                                                # Get the latitude and longitude data.
                                                LAT   = np.array(getvar(ncfile, "XLAT"))
                                                latitudes = (LAT[:,0])
                                                LONG  = np.array(getvar(ncfile, "XLONG"))
                                                longitudes = (LONG[0,:])
                                                # Get the sea level pressure for each wrf output file.
                                                slp2D = np.array(getvar(ncfile, "slp", Time_Idx))

                                                # Get theindex of the minimum value of pressure.
                                                idx = np.where(slp2D == np.amin(slp2D))

                                                # List the data of the minimum SLP
                                                min_slp.append(np.amin(slp2D))
                                                min_lat.append(float(latitudes[idx[0][0]]))
                                                min_long.append(float(longitudes[idx[1][0]]))
                                                #get the 2D field of kpbl values
                                                
                                                kpbl=np.array(getvar(ncfile,"KPBL", Time_Idx))
                                                #reducie it into 1D
                                                kpbl=kpbl.flatten()
                        



                                                PBLH_2D = np.array(getvar(ncfile,"PBLH", Time_Idx))
                                                U10_2D = np.array(getvar(ncfile, "U10", Time_Idx))
                                                V10_2D = np.array(getvar(ncfile, "V10", Time_Idx))
                                                PBLH_1D=PBLH_2D.flatten()
                                                U10_1D = U10_2D.flatten()
                                                V10_1D = V10_2D.flatten()
                                                WND_SPD_10 = U10_1D
                                                # Calculate the wind intensity at each point of the map.
                                                for i in range (WND_SPD_10.size - 1):
                                                        WND_SPD_10[i] = math.sqrt((U10_1D[i]**2)+(V10_1D[i]**2))

                                                # Search for the maximum wind intensity at aspecific time step. 
                                                WND_SPD_10_max = np.amax(WND_SPD_10)

                                                # List the maximum wind intensity for all time steps.   
                                                All_Max_WND_SPD_10.append(WND_SPD_10_max)
        
                                                #create an empy list for storing 100 PBLH, and their levels
                                                list_of_PBLHS = []
                                                list_of_kpbls =[]
                                                list_of_mid_pbl_lvls =[]
                                                
                                                list_of_exch_lvl_0=[]
                                                list_of_exch_lvl_1=[]
                                                list_of_exch_lvl_2=[]
                                                list_of_exch_lvl_3=[]
                                                list_of_exch_lvl_4=[]
                                                list_of_exch_lvl_5=[]
                                                list_of_exch_lvl_6=[]
                                                list_of_exch_lvl_7=[]
                                                

                                                list_of_exch_ms = []
                                                list_of_exch_ms_mid_pbl=[]

                                                #get the indices for 100 highest values of wind intensity
                                                
                                                top_100_idx = np.argsort(WND_SPD_10)[-100:]
                                                for idx in top_100_idx:
                                                        #get the top pbl lvls for 10 highest winds
                                                        list_of_kpbls.append(round(kpbl[idx]))
                                                #average it into a single number and get the mid pbl
                                                if counter_for_mid_pbl == 0: 
                                                        mid_pbl_height_lvl=int(round(np.average(list_of_kpbls))/2)
                                                        list_of_mid_pbl_lvls.append(mid_pbl_height_lvl)

                                                #get the vertical exchange coefficients
                                                #note: MYJ has only EXCH_H but it's equal to exch_m if prandtl =1
                                                #YSU has actual values of exch_m
                                                #Also MYJ has exchanges at 0th node, whereas YSU is all zeroes at 0th node!
                                                exch=[]
                                                if PBL == 'MYJ':
                                                
                                                        EXCH_M_3D=np.array(getvar(ncfile,"EXCH_H", Time_Idx))
                                                elif PBL == 'ACM2' or 'ACM2_additional_changs':
                                                        EXCH_M_3D=np.array(getvar(ncfile,"EDDYZM", Time_Idx))
                                                       
                                                else:
                                                        EXCH_M_3D=np.array(getvar(ncfile,"EXCH_M", Time_Idx))
                                                if ncfile_counter >1:
                                                        for i in range(len(z)):
                                                                lvl_heights.append(np.average(z[i].flatten()[top_100_idx]))                                
                                                                vert_exch_vert_prof.append(np.average(EXCH_M_3D[i].flatten()[top_100_idx]))
                                                        plt.plot(vert_exch_vert_prof,lvl_heights)
                                                        print(shape(EXCH_M_3D))
                                                        plt.show()
                                                

                                        #         if ncfile_counter==int(len(ncfiles)/2):
                                                        
                                        #                 print('mid ncfile number:',ncfile_counter)
                                        #                 for i in range(len(z)):
                                        #                         lvl_heights.append(np.average(z[i].flatten()[top_100_idx]))                                
                                        #                         vert_exch_vert_prof.append(np.average(EXCH_M_3D[i].flatten()[top_100_idx]))



                                                        


                                        #         EXCH_M_2D_lvl_0=EXCH_M_3D[0,:,:].flatten()
                                        #         EXCH_M_1D_lvl_0=EXCH_M_2D_lvl_0.flatten()

                                        #         EXCH_M_2D_lvl_1=EXCH_M_3D[1,:,:].flatten()
                                        #         EXCH_M_1D_lvl_1=EXCH_M_2D_lvl_1.flatten()

                                        #         EXCH_M_2D_lvl_2=EXCH_M_3D[2,:,:].flatten()
                                        #         EXCH_M_1D_lvl_2=EXCH_M_2D_lvl_2.flatten()

                                        #         EXCH_M_2D_lvl_3=EXCH_M_3D[3,:,:].flatten()
                                        #         EXCH_M_1D_lvl_3=EXCH_M_2D_lvl_3.flatten()

                                        #         EXCH_M_2D_lvl_4=EXCH_M_3D[4,:,:].flatten()
                                        #         EXCH_M_1D_lvl_4=EXCH_M_2D_lvl_4.flatten()

                                        #         EXCH_M_2D_lvl_5=EXCH_M_3D[5,:,:].flatten()
                                        #         EXCH_M_1D_lvl_5=EXCH_M_2D_lvl_5.flatten()

                                        #         EXCH_M_2D_lvl_6=EXCH_M_3D[6,:,:].flatten()
                                        #         EXCH_M_1D_lvl_6=EXCH_M_2D_lvl_6.flatten()

                                        #         EXCH_M_2D_lvl_7=EXCH_M_3D[7,:,:].flatten()
                                        #         EXCH_M_1D_lvl_7=EXCH_M_2D_lvl_7.flatten()

                                        #         EXCH_M_2D_mid_pbl=EXCH_M_3D[mid_pbl_height_lvl,:,:].flatten()

                                        #         EXCH_M_1D_mid_pbl=EXCH_M_2D_mid_pbl.flatten()
                                                
                                        #         #Create a list of PBLH values on indices of 100 highest values of wind intensity
                                        #         for idx in top_100_idx:
                                        #                 list_of_exch_lvl_0.append(EXCH_M_1D_lvl_0[idx])
                                        #                 list_of_exch_lvl_1.append(EXCH_M_1D_lvl_1[idx])
                                        #                 list_of_exch_lvl_2.append(EXCH_M_1D_lvl_2[idx])
                                        #                 list_of_exch_lvl_3.append(EXCH_M_1D_lvl_3[idx])
                                        #                 list_of_exch_lvl_4.append(EXCH_M_1D_lvl_4[idx])
                                        #                 list_of_exch_lvl_5.append(EXCH_M_1D_lvl_5[idx])
                                        #                 list_of_exch_lvl_6.append(EXCH_M_1D_lvl_6[idx])
                                        #                 list_of_exch_lvl_7.append(EXCH_M_1D_lvl_7[idx])

                                        #                 list_of_PBLHS.append(PBLH_1D[idx])

                                        #                 list_of_exch_ms_mid_pbl.append(EXCH_M_1D_mid_pbl[idx])
                                        #         #avergae the 100 values into 1 and add it to a list
                                        #         average_exch_lvl_0.append(np.average(list_of_exch_lvl_0))
                                        #         average_exch_lvl_1.append(np.average(list_of_exch_lvl_1))
                                        #         average_exch_lvl_2.append(np.average(list_of_exch_lvl_2))
                                        #         average_exch_lvl_3.append(np.average(list_of_exch_lvl_3))
                                        #         average_exch_lvl_4.append(np.average(list_of_exch_lvl_4))
                                        #         average_exch_lvl_5.append(np.average(list_of_exch_lvl_5))
                                        #         average_exch_lvl_6.append(np.average(list_of_exch_lvl_6))
                                        #         average_exch_lvl_7.append(np.average(list_of_exch_lvl_7))

                                        #         average_PBLHS.append(np.average(list_of_PBLHS))
                                        #         average_kpbls.append(np.average(list_of_kpbls))
                                        #         average_exch_ms_mid_pbl.append(np.average(list_of_exch_ms_mid_pbl))
                                        #         average_mid_lvl_pbl.append(np.average(list_of_mid_pbl_lvls))

                                        
                                
                                        # counter_for_mid_pbl =1
                                        
                                                ##############################
                                                # Exporting the simulated data #
                                                ##############################
                                        # print('finallr eetracted everything, now just let me write it up!')
                                        # create_file (Output_Dir, HN)
                                        # create_file (Output_Dir + HN + '/', GS)
                                        # Path = os.getcwd()
                                        # print ('Writing into: ',Path)
                                        # print(len(average_PBLHS))
                                        # print(len(lvl_heights))

                                        # MyFile=open('%s.csv' %Hurricane_Setting,'w')

                                        # MyFile.write (Hurricane_Setting + "\n")
                                        # MyFile.write ("lvl_heights,avg_vert_exch,PBLH,kpbl,All_Max_WND_SPD_10,min_lat,min_long,min_slp,exch_lvl_0,exch_lvl_1,exch_lvl_2,exch_lvl_3,exch_lvl_4,exch_lvl_5,exch_lvl_6,exch_lvl_7,exch_m_mid_pbl,mid_lvl_pbl\n")
                                        # for i in range(len(average_PBLHS)):
                                                        
                                        #                 MyFile.write (str(lvl_heights[i]) + ","
                                        #                                 + str(vert_exch_vert_prof[i]) + ","
                                        #                                 + str(average_PBLHS[i]) + ","
                                        #                                 + str(average_kpbls[i]) + ","
                                        #                                 + str(All_Max_WND_SPD_10[i]) + ","
                                        #                                 + str(min_lat[i]) + "," 
                                        #                                 + str(min_long[i]) + "," 
                                        #                                 + str(min_slp[i]) + "," 
                                        #                                 + str(average_exch_lvl_0[i]) + ","
                                        #                                 + str(average_exch_lvl_1[i]) + ","
                                        #                                 + str(average_exch_lvl_2[i]) + ","
                                        #                                 + str(average_exch_lvl_3[i]) + ","
                                        #                                 + str(average_exch_lvl_4[i]) + ","
                                        #                                 + str(average_exch_lvl_5[i]) + ","
                                        #                                 + str(average_exch_lvl_6[i]) + ","
                                        #                                 + str(average_exch_lvl_7[i]) + ","
                                        #                                 + str(average_exch_ms_mid_pbl[i]) + ","
                                        #                                 + str(average_mid_lvl_pbl[i])+ "\n")
                                                
                                        # for i in range(len(vert_exch_vert_prof)-len(average_PBLHS)):
                                        #                 MyFile.write (str(lvl_heights[i+len(average_PBLHS)]) + ","
                                        #                                 + str(vert_exch_vert_prof[i+len(average_PBLHS)])+ "\n")
                                        
                               
                                        # MyFile.close()
