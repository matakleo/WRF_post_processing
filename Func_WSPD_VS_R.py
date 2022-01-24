from Func_Hurricane_Eye import hurricane_eye_3
from Func_Distances import Calculate_Distance_Haversine
from wrf import getvar, interplevel
from netCDF4 import Dataset
import numpy as np
import math
from wrf import interplevel




####################################################################
# This function plot the average WSPD in terms of radii intervals. #
####################################################################

def Extract_WSPD_VS_Radius (ncfile, Time_idx, Z_WSPD, DR):
		
	print ('Working on the ', Time_idx, 'th hour of ', ncfile)
	# These lists will contain the final data.
	Average_WSPD = []
	Normalized_Average_WSPD = []
	Radiuses = [i for i in range (0, 501, DR)]
	Normalized_Radiuses = []

	# This dictionnary will contain the wspd in terms of radius. 
	WSPD_VS_R = {i:[] for i in range (0, 501, DR)}

	# Extracting the data.
	Data = Dataset(ncfile)
	Lats = np.array(getvar (Data, 'XLAT')[:,0])
	Lons = np.array(getvar (Data, 'XLONG')[0,:])
	Z_3D = np.array(getvar (Data, 'z'))
	WSPD_3D = np.array(getvar (Data, 'wspd'))
	WSPD_2D = interplevel(WSPD_3D, Z_3D, Z_WSPD)
	Max_WSPD = np.max(WSPD_2D)
	Idx_Max_WSPD = np.where(WSPD_2D == Max_WSPD)
	Lat_Max_WSPD = Lats[Idx_Max_WSPD[0]]
	Lon_Max_WSPD = Lons [Idx_Max_WSPD[1]]
	(Eye_Slp, Eye_Idx, Eye_Xlat, Eye_Xlon) = hurricane_eye_3(Data, Time_idx)
	R_Max_WSPD = Calculate_Distance_Haversine (Lat_Max_WSPD, Lon_Max_WSPD, Eye_Xlat, Eye_Xlon)
	Eye_WSPD = float(WSPD_2D[Eye_Idx[0], Eye_Idx[1]])
	# Printing a summary of the data.
	print ('Max_WSPD =', float(Max_WSPD))
	print ('Eye_WSPD =', Eye_WSPD)
	print ('R_Max_WSPD =', R_Max_WSPD)
	#print ('Idx_Max_WSPD  =', Idx_Max_WSPD )


# Calculate the wspd in terms of the radius and fill in the dictionnary.
	for Lat in Lats:
		for Lon in Lons:
			D = Calculate_Distance_Haversine (Lat, Lon, Eye_Xlat, Eye_Xlon)
			Lat_idx = np.where(Lats == Lat)
			Lon_idx = np.where(Lons == Lon)
			for i in range (0, 501, DR):
				if ((i-(DR/2))<D) and (D<(i+(DR/2))):
					WSPD_VS_R[i].append(float(WSPD_2D[Lat_idx[0], Lon_idx[0]]))

	# Calculate the average wspd and fill the list.
	for i in range (0, 501, DR):
		#print (i)
		Average = 0
		for WSPD in WSPD_VS_R[i]:
			Average += WSPD
		#print (Average)
		if ((Average != 0) and (math.isnan(Average) == False)):
			#print (len(WSPD_VS_R[i]))
			Average = Average/len(WSPD_VS_R[i])
			Average_WSPD.append(Average)
		elif (Average == 0) or (math.isnan(Average)):
			Radiuses.remove(i)

	# Calculate the normalized average wspd and fill the list.
	Max_Average_WSPD = np.max(Average_WSPD)
	Idx_Max_Average_WSPD = np.where(Average_WSPD == Max_Average_WSPD)
	R_Max_Average_WSPD = Radiuses[int(Idx_Max_Average_WSPD[0])]
	for i in range (len(Average_WSPD)):
		
		try:
			Normalized_Average_WSPD.append(Average_WSPD[i]/Max_Average_WSPD)
			Normalized_Radiuses.append(Radiuses[i]/R_Max_Average_WSPD)
		except (ZeroDivisionError):
			print ('R_Max_Average_WSPD = ', R_Max_Average_WSPD, ' : Normalized_Radiuses will be given the value of R_Max_Average_WSPD')
			Normalized_Average_WSPD = Average_WSPD/Max_Average_WSPD
			Normalized_Radiuses = Radiuses
			break
	#print (len(Radiuses))
	#print (len(Average_WSPD))
	#print (len(Normalized_Radiuses))
	#print (len(Normalized_Average_WSPD))
	return (Radiuses, Average_WSPD, Normalized_Radiuses, Normalized_Average_WSPD)

		
