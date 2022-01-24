
from Func_WSPD_VS_SLP import Extract_WSPD_VS_SLP
from Func_List_Files import list_ncfiles
import os

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

# Choose between : 'Gustav', 'Irma', 'Katrina', 'Maria'
HNS = ['Irma']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['4km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TMS = ['NoTurb']
# Choose between : 'YSU', 'MYJ', 'ACM2'
PBLS = ['YSU','YSU_additional_changs','ACM2','ACM2_additional_changs']
# Choose between : 'cLh0p2', 'cLh0p5', 'cLh1p0', 'cLh1p5'
CLS = ['250','500','1000','2000','1.0','xkzm_0.25','xkzm_4.0','lvl_2','lvl_4','lvl_8']
# Set the input directory.
Input_Dir = '/project/momen/Lmatak/WRF/Hurricanes/'
Output_Dir = '/project/momen/Lmatak/WRF/Hurricanes/pblh_data/fixed_hpbls/'
# Choose between: '0', '1', '2', '3', '4', '5'
Time_idxs = [0]

#Choose a radius interval
DSLP = 4
# Choose an altitude
Z_WSPD = 500


# Check the simulations to be working on.

for HN in HNS:
        for GS in GSS:
                for TM in TMS:
                        for PBL in PBLS:
                                for CL in CLS:
                                        Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL + '_hpbl_' + CL

                                        Input_Dir_1 = Input_Dir + HN + '/' + GS + '/HPBL_SENSITIVITY/'  + PBL +'/'+ TM + '/'+ Hurricane_Setting
                                        ncfiles = []
                                        ncfiles = list_ncfiles (Input_Dir_1, ncfiles)
                                        ncfile_number=int(len(ncfiles)/2)
                                        ncfile=ncfiles[ncfile_number]

                                        for Time_idx in Time_idxs:
                                                        # Extracting wspd in terms of radius.
                                                        os.chdir(Input_Dir_1)
                                                        try:
                                                                (SLPS, Average_WSPD, Normalized_SLPS, Normalized_Average_WSPD) = Extract_WSPD_VS_SLP (ncfile, Time_idx, Z_WSPD, DSLP)
                                                        except (IndexError):
                                                                print (ncfile, 'contains only one hour of simulation')
                                                                break
                                                        # Exporting the data in a csv format.
                                                        create_file (Output_Dir, 'WSPD_VS_SLP')
                                                        create_file (Output_Dir + 'WSPD_VS_SLP/', 'WSPD_VS_SLP_' + str(DSLP))
                                                        create_file (Output_Dir + 'WSPD_VS_SLP/' + 'WSPD_VS_SLP_' + str(DSLP) + '/', HN)
                                                        create_file (Output_Dir + 'WSPD_VS_SLP/' + 'WSPD_VS_SLP_' + str(DSLP) + '/' + HN + '/', GS)
                                                        create_file (Output_Dir + 'WSPD_VS_SLP/' + 'WSPD_VS_SLP_' + str(DSLP) + '/' + HN + '/' + GS + '/', Hurricane_Setting)
                                                        file_name = ncfile + '_' + str(Time_idx)
                                                        MyFile=open("%s.csv" %file_name,'w')
                                                        MyFile.write ("SLPS, Average_WSPD, Normalized_SLPS, Normalized_Average_WSPD" + "\n")
                                                        for n in range (len(SLPS)):
                                                                MyFile.write (str(SLPS[n]) + ',' + str(Average_WSPD[n]) + ',' + str(Normalized_SLPS[n]) + ',' + str(Normalized_Average_WSPD[n]) + "\n")


