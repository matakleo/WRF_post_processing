from math import e
from Func_Distances import Calculate_Distance_Haversine

def Calculate_Error_Intensity (V_Forecast, Real_Output, Error_List, Average_Error):

	count = len (V_Forecast)
	Error = 0
	for i in range (count):
		Error =(abs (V_Forecast [i] - Real_Output [i]) / Real_Output [i])
		Error_List.append(Error)
	count_1 = len (Error_List)
	for Error in Error_List:	
		Average_Error += Error
	Average_Error /= count_1
	list.sort (Error_List)
	return (Error_List, Average_Error)



def Calculate_Error_Track (Lat_Forecast, Lon_Forecast, Lat_Best, Lon_Best, Error_List, Average_Error):

	count = len (Lat_Forecast)
	Error = 0
	for i in range (count):
		Error = Calculate_Distance_Haversine (Lat_Forecast[i], Lon_Forecast[i], Lat_Best[i], Lon_Best[i])
		Error_List.append(Error)
	count_1 = len (Error_List)
	for Error in Error_List:
		Average_Error += Error
	Average_Error /= count_1
	list.sort (Error_List)
	return (Error_List, Average_Error)


def Calculate_Error_Track_2 (Lat_Forecast, Lon_Forecast, Lat_Best, Lon_Best, Error_List):

	count = len (Lat_Forecast)
	Error = 0
	for i in range (count):
		Error = Calculate_Distance_Haversine (Lat_Forecast[i], Lon_Forecast[i], Lat_Best[i], Lon_Best[i])
		Error_List.append(Error)
	count_1 = len (Error_List)
	for Error in Error_List:
		Average_Error += Error
	Average_Error /= count_1
	list.sort (Error_List)
	return (Error_List, Average_Error)

def Calculate_Error_Intensity_2 (wspd_List, V_Best, Error_List, Average_Error_List):
	#print(wspd_List)

	Counter = len (wspd_List)
	Error = 0
	for i in range (Counter):
		
		Error_Per_TS =(abs (wspd_List [i] - V_Best[i]) / V_Best[i])
		# print('moj wind: ',wspd_List[i])
		# print('best wind: ',V_Best[i])
		Error_List.append(Error_Per_TS)
		Error += Error_Per_TS
	Error /= Counter
	Average_Error_List.append(Error)
	list.sort (Error_List)

def Calculate_Error_Track_3 (Lat_Forecast, Lon_Forecast, Lat_Best, Lon_Best, Average_Error_List):
  Average_Error_List=[]
  Counter = len (Lat_Forecast)
  Error = 0
  for i in range (Counter):
    Error_Per_TS = Calculate_Distance_Haversine (Lat_Forecast[i], Lon_Forecast[i], Lat_Best[i], Lon_Best[i])
    
    Error += Error_Per_TS
  Error /= Counter
  Average_Error_List.append(Error)

def calculate_distance_error (eye_lats,eye_longs,best_lats,best_longs):
	errorz=0
	# print(len(eye_lats),len(eye_longs),len(best_lats),len(best_longs))
	for i in range(len(eye_lats)):
		error=Calculate_Distance_Haversine(eye_lats[i],eye_longs[i],best_lats[i],best_longs[i])
		errorz += error/len(eye_lats)
	return errorz
def calculate_intensity_error (simulated_vars,real_vars):
	error=0
	# print(len(simulated_vars),len(real_vars))
	for i in range(len(simulated_vars)):
		error += (abs(simulated_vars[i]-real_vars[i])/real_vars[i])/len(simulated_vars)
	# print('error:',error)

	return error*100

def calculate_intensity_error_slp (simulated_vars,real_vars):
	error=0
	# print(len(simulated_vars),len(real_vars))
	for i in range(len(simulated_vars)):
		error += (abs(simulated_vars[i]-real_vars[i])/real_vars[i])
	# print('error:',error)

	return error*100

  