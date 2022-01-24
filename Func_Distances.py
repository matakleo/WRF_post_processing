from math import sin, cos, sqrt, atan2, radians
import numpy as np






#######################################################################################
# This function calculates the distance between two geographic points using Haversine #
# formula                                                                             #
#######################################################################################

def Calculate_Distance_Haversine (Lat_1, Long_1, Lat_2, Long_2):
	# approximate radius of earth in km
	R = 6373.0
	Lat_1 = radians(Lat_1)
	Long_1 = radians(Long_1)
	Lat_2 = radians(Lat_2)
	Long_2 = radians(Long_2)

	Dlong = Long_2 - Long_1
	Dlat = Lat_2 - Lat_1

	a = sin(Dlat / 2)**2 + cos(Lat_1) * cos(Lat_2) * sin(Dlong / 2)**2
	c = 2 * np.arcsin(sqrt(a))

	distance = R * c
	return (distance)