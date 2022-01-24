from netCDF4 import Dataset
import os
from wrf import getvar
import numpy as np
import csv


# This function extracts the real track data.

def Extract_Track_Data (Real_Data_Dir, List, Variable_Name,HN):
	os.chdir(Real_Data_Dir)
	with open('Real_Data_'+HN+'.csv') as f:
		reader = csv.reader(f)
	#	next (reader)
		row_header = next(reader)
		#print (row_header)
		for row in reader:
			if row[row_header.index(Variable_Name)] == '': continue
			List.append(float(row[row_header.index(Variable_Name)]) )
	return (List)

	
def Extract_by_name (Output_File, list_name, variable_name):
	with open(Output_File) as f:
		reader = csv.reader(f)
		if (Output_File.find('Real_Data') == -1):
			next (reader)
		row_header = next(reader)


		for row in reader:
			# print(row)

			try:
				if (row[row_header.index(variable_name)]) == '' : continue
				if variable_name== 'Wind Speed(kt)':
					list_name.append(0.51444 * float(row[row_header.index(variable_name)]))
				
				else:
					list_name.append(float(row[row_header.index(variable_name)]) )
			except: continue
	return (list_name)


def Extract_the_shit2 (Output_File, list_name, variable_name):
	with open(Output_File) as f:
		reader = csv.reader(f)
		row_header = next(reader)

		for row in reader:
			try:
				if (row[row_header.index(variable_name)]) == '' : continue
				if variable_name== 'Wind Speed(kt)':
					list_name.append(0.51444 * float(row[row_header.index(variable_name)]))
				
				else:
					list_name.append(float(row[row_header.index(variable_name)]) )
			except: continue
	return (list_name)




def Extract_Coordinates_2 (Dir, Forecast_Outputs, Lat_Header, Lon_Header):
	os.chdir(Dir)
	Lat_Forecast = []
	Lon_Forecast = []
	with open(Forecast_Outputs) as f:
		reader = csv.reader(f)
		next (reader)
		row_header = next(reader)
		#print (row_header)
		for row in reader:
			try:
				if row[row_header.index(Lat_Header)] == '': continue
				if row[row_header.index(Lon_Header)] == '': continue
				Lat_Forecast.append(float(row[row_header.index(Lat_Header)]))
				Lon_Forecast.append(float(row[row_header.index(Lon_Header)]))
			except:continue
	return (Lat_Forecast, Lon_Forecast)

def flatten_the_curve (list_of_data):
	flattened_list_of_data=[]
	for i in range(len(list_of_data)):
		if i == 0:
			flattened_list_of_data.append(list_of_data[i])
		else:
			flattened_list_of_data.append((list_of_data[i]+list_of_data[i-1])/2)
	return flattened_list_of_data

