
from Func_WSPD_VS_R import Extract_WSPD_VS_Radius
from Func_List_Files import list_ncfiles
from export_everything import create_file
import os



# Choose between : 'Gustav', 'Irma', 'Katrina', 'Maria'
HNS = ['Irma']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['4km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TMS = ['NoTurb']
# Choose between : 'YSU', 'MYJ', 'ACM2'
PBLS = ['YSU','YSU_additional_changs','ACM2','ACM2_additional_changs']
# Choose between : 'cLh0p2', 'cLh0p5', 'cLh1p0', 'cLh1p5'
CLS = ['1.0']
# Set the input directory.
Input_Dir = '/project/momen/Lmatak/WRF/Hurricanes/'
Output_Dir = '/project/momen/Lmatak/WRF/Hurricanes/pblh_data/fixed_hpbls/'
# Choose between: '0', '1', '2', '3', '4', '5'
Time_idxs = [0, 1, 2, 3, 4, 5]
#Choose a radius interval
DR = 4
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

                                        for ncfile in ncfiles:
                                                for Time_idx in Time_idxs:
                                                        # Extracting wspd in terms of radius.
                                                        os.chdir(Input_Dir_1)
                                                        try:
                                                                (Radiuses, Average_WSPD, Normalized_Radiuses, Normalized_Average_WSPD) = Extract_WSPD_VS_Radius (ncfile, Time_idx, Z_WSPD, DR)
                                                        except (IndexError):
                                                                print (ncfile, 'contains only one hour of simulation')
                                                                break
                                                        # Exporting the data in a csv format.
                                                        create_file (Output_Dir, 'WSPD_VS_Radius')
                                                        create_file (Output_Dir + 'WSPD_VS_Radius/', 'WSPD_VS_Radius_' + str(DR))
                                                        create_file (Output_Dir + 'WSPD_VS_Radius/' + 'WSPD_VS_Radius_' + str(DR) + '/', HN)
                                                        create_file (Output_Dir + 'WSPD_VS_Radius/' + 'WSPD_VS_Radius_' + str(DR) + '/'+ HN + '/', GS)
                                                        create_file (Output_Dir + 'WSPD_VS_Radius/' + 'WSPD_VS_Radius_' + str(DR) + '/'+ HN + '/' + GS + '/', Hurricane_Setting)
                                                        file_name = ncfile + '_' + str(Time_idx)
                                                        MyFile=open("%s.csv" %file_name,'w')
                                                        MyFile.write ("Radiuses, Average_WSPD, Normalized_Radiuses, Normalized_Average_WSPD" + "\n")
                                                        for n in range (len(Radiuses)):
                                                                MyFile.write (str(Radiuses[n]) + ',' + str(Average_WSPD[n]) + ',' + str(Normalized_Radiuses[n]) + ',' + str(Normalized_Average_WSPD[n]) + "\n")



