from wrf import getvar, interplevel
from netCDF4 import Dataset
import numpy as np
import math
from wrf import interplevel




####################################################################
# This function plot the average WSPD in terms of radii intervals. #
####################################################################

def Extract_WSPD_VS_SLP (ncfile, Time_idx, Z_WSPD, DSLP):
		
	print ('Working on the ', Time_idx, 'th hour of ', ncfile)
	# These lists will contain the final data.
	Average_WSPD = []
	Normalized_Average_WSPD = []
	SLPS = [i for i in range (925, 1010, DSLP)]
	Normalized_SLPS = []

	# This dictionnary will contain the wspd in terms of radius. 
	WSPD_VS_SLP = {i:[] for i in range (925, 1010, DSLP)}

	# Extracting the data.
	Data = Dataset(ncfile)
	SLP = np.array(getvar (Data, 'slp'))
	Z_3D = np.array(getvar (Data, 'z'))
	WSPD_3D = np.array(getvar (Data, 'wspd'))
	WSPD_2D = interplevel(WSPD_3D, Z_3D, Z_WSPD)
	Max_WSPD = np.max(WSPD_2D)

	# Calculate the wspd in terms of SLP and fill in the dictionnary.
	for i in range (len(SLP[:,0])):
		for j in range (len(SLP[0,:])):
			for k in range (925, 1010, DSLP):
				if ((k-(DSLP/2))<SLP[i,j]) and (SLP[i,j]<(k+(DSLP/2))):
					if not (math.isnan(WSPD_2D[i, j])):
						WSPD_VS_SLP[k].append(float(WSPD_2D[i, j]))
	
	# Calculate the average wspd and fill the list.
	for i in range (925, 1010, DSLP):
		#print (i)
		Average = 0
		for WSPD in WSPD_VS_SLP[i]:
			Average += WSPD
		#print (Average)
		if ((Average != 0) and (math.isnan(Average) == False)):
			#print (len(WSPD_VS_R[i]))
			Average = Average/len(WSPD_VS_SLP[i])
			Average_WSPD.append(Average)
		elif (Average == 0) or (math.isnan(Average)):
			SLPS.remove(i)

	# Calculate the normalized average wspd and fill the list.
	Max_Average_WSPD = np.max(Average_WSPD)
	Idx_Max_Average_WSPD = np.where(Average_WSPD == Max_Average_WSPD)
	SLP_Max_Average_WSPD = SLPS[int(Idx_Max_Average_WSPD[0])]
	for i in range (len(Average_WSPD)):
		Normalized_Average_WSPD.append(Average_WSPD[i]/Max_Average_WSPD)
		Normalized_SLPS.append(SLPS[i]/SLP_Max_Average_WSPD)
		

	print (SLPS)
	print (Average_WSPD)
	#print (len(Normalized_SLPS))
	#print (len(Normalized_Average_WSPD))
	return (SLPS, Average_WSPD, Normalized_SLPS, Normalized_Average_WSPD)

		
