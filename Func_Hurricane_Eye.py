import numpy as np
from wrf import getvar




# This function returns the hurricane's eye SLP, XLAT, XLONG and WSPD using a dictionnary data.
def hurricane_eye(Data, ncfile, Time_idx):

	# Get the index of the minimum value of pressure.
	idx = np.where(Data[ncfile][Time_idx]['slp'] == np.amin(Data[ncfile][Time_idx]['slp']))
	Eye_Slp = np.amin(Data[ncfile][Time_idx]['slp'])
	Eye_Xlat = float (Data[ncfile][Time_idx]['XLAT'][idx])
	Eye_Xlong = float (Data[ncfile][Time_idx]['XLONG'][idx])
	return (Eye_Slp, Eye_Xlat, Eye_Xlong)

# This function returns the hurricane's eye SLP, XLAT, XLONG and WSPD using SLP, LAT and LONG.
def hurricane_eye_2(SLP, LAT, LONG):
	idx = np.where(np.array(SLP) == np.amin(np.array(SLP)))
	Eye_Slp = np.amin(np.array(SLP))
	Eye_Xlat = float (np.array(LAT)[idx])
	Eye_Xlong = float (np.array(LONG)[idx])
	return (Eye_Slp, Eye_Xlat, Eye_Xlong)


# This function returns the hurricane's eye SLP, XLAT, XLONG and WSPD using the original data.
def hurricane_eye_3(Data, Time_idx):

		# The Data here is the ncfile.
		SLP = np.array(getvar(Data, 'slp', Time_idx))
		Eye_Slp = np.amin(SLP) 
		Eye_Idx = np.where(SLP == np.amin(SLP))
		Eye_Xlat = float (np.array(getvar (Data, 'XLAT', Time_idx))[Eye_Idx])
		Eye_Xlong = float (np.array(getvar (Data, 'XLONG', Time_idx))[Eye_Idx])
		return (Eye_Slp, Eye_Idx, Eye_Xlat, Eye_Xlong)