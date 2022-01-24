import os



# This function returns a list of all wrf ouput files in the directory.
def list_ncfiles(Dir, ncfiles):
	for f in os.listdir(Dir):
		if f.startswith('wrfout'):
			ncfiles.append(f)
	ncfiles.sort()
	return (ncfiles)

def list_csv_files_0(Dir,list_with_csv_targets):
	os.chdir(Dir)
	csv_files=[]
	for csv_file in list_with_csv_targets:
		for f in os.listdir(Dir):
			if (f.find(csv_file) != -1):
				csv_files.append(f)
	return(csv_files)

def list_csv_files (Dir, csv_files):
	for f in os.listdir(Dir):
		if (f == "Real_Output.csv"):
			csv_files.append(f)
		#if (f == "Dropsonde.csv"):
		#	csv_files.append(f)
		elif (f.find('Smag2D') != -1) and (f.find('cLh1p0') != -1):
			csv_files.append(f)
		elif (f.find('NoTurb') != -1) and (f.find('cLh1p0') != -1):
			csv_files.append(f)
		elif (f.find('TKE2D') != -1) and (f.find('cLh1p0') != -1):
			csv_files.append(f)
	return (csv_files)

def list_csv_files_1 (Dir, Forecast_Outputs_pfac_1p5,Forecast_Outputs_pfac_2p0, Forecast_Outputs_pfac_3p0,Real_Output):

	for f in os.listdir(Dir):
		if (f == "Real_Output.csv"):
			Real_Output = f


		elif (f.find('_pfac_1.5.') != -1):
			Forecast_Outputs_pfac_1p5 = f
		elif (f.find('_pfac_2.0.') != -1):
			Forecast_Outputs_pfac_2p0 = f
		elif (f.find('_pfac_3.0.') != -1):
			Forecast_Outputs_pfac_3p0 = f


	
	
	return (  Forecast_Outputs_pfac_1p5,Forecast_Outputs_pfac_2p0, Forecast_Outputs_pfac_3p0,
			 Real_Output)

def list_csv_files_2 (Dir, csv_files, TM):
	for f in os.listdir(Dir):
		if (f == "Real_Output.csv"):
			csv_files.append(f)
		if (f == "Dropsonde.csv"):
			csv_files.append(f)
		elif (f.find(TM) != -1):
			csv_files.append(f)
	return (csv_files)

def list_csv_files_3 (Dir, csv_files):
	for f in os.listdir(Dir):
		if f=='.DS_Store':
			pass
		else:
			csv_files.append(f)
	csv_files.sort()
	return (csv_files)

def list_hurricane_settings(Dir, Hurricane_Simulations):
	for f in os.listdir(Dir):
		if f=='.DS_Store':
			pass
		else:
			Hurricane_Simulations.append(f)
	Hurricane_Simulations.sort()
	return (Hurricane_Simulations)

def list_files_4 (Dir_2, TM, Forecast_Outputs_0p2, Forecast_Outputs_0p5, Forecast_Outputs_1p0, Forecast_Outputs_1p5, Real_Output):
	for f in os.listdir(Dir_2):
		if (f == "Real_Output.csv"):
			Real_Output = f
		elif (f.find('0p2') != -1) and (f.find(TM) != -1):
			Forecast_Outputs_0p2 = f
		elif (f.find('0p5') != -1) and (f.find(TM) != -1):
			Forecast_Outputs_0p5 = f
		elif (f.find('1p0') != -1) and (f.find(TM) != -1):
			Forecast_Outputs_1p0 = f
		elif (f.find('1p5') != -1) and (f.find(TM) != -1):
			Forecast_Outputs_1p5 = f
	return (Forecast_Outputs_0p2, Forecast_Outputs_0p5, Forecast_Outputs_1p0, Forecast_Outputs_1p5, Real_Output)

def list_files_5 (Dir, Hurricane, NDay, TM, CLH):
	Dir_1 = Dir + Hurricane + '/32km_REF_' + NDay + '/'
	Forecast_Outputs = ''
	for f in os.listdir(Dir_1):
		#print (f)
		#print (CLH)
		if (f.find(CLH)!= -1) and (f.find(TM) != -1):
			Forecast_Outputs = f
			#print (Forecast_Outputs)
	return (Forecast_Outputs, Dir_1)

def list_files_6 (Dir, Hurricane, NDay, TM, CLH):
	Dir_1 = Dir + Hurricane + '/'
	Forecast_Outputs = ''
	for f in os.listdir(Dir_1):
		#print (f)
		#print (CLH)
		if (f.find(CLH)!= -1) and (f.find(TM) != -1) and (f.find(NDay) != -1):
			Forecast_Outputs = f
			#print (Forecast_Outputs)
	return (Forecast_Outputs, Dir_1)

def list_files_7 (Dir, TM, Forecast_Outputs_0p1, Forecast_Outputs_0p2, Forecast_Outputs_0p5, Forecast_Outputs_1p0, Forecast_Outputs_1p5, Real_Output):
        for f in os.listdir(Dir):
          if (f == "Real_Output.csv"):
            Real_Output = f
          elif (f.find('0p1') != -1) and (f.find(TM) != -1):
            Forecast_Outputs_0p1 = f
          elif (f.find('0p2') != -1) and (f.find(TM) != -1):
            Forecast_Outputs_0p2 = f
          elif (f.find('0p5') != -1) and (f.find(TM) != -1):
            Forecast_Outputs_0p5 = f
          elif (f.find('1p0') != -1) and (f.find(TM) != -1):
            Forecast_Outputs_1p0 = f
          elif (f.find('1p5') != -1) and (f.find(TM) != -1):
            Forecast_Outputs_1p5 = f
        return (Forecast_Outputs_0p1, Forecast_Outputs_0p2, Forecast_Outputs_0p5, Forecast_Outputs_1p0, Forecast_Outputs_1p5, Real_Output)

# Identify all possible settings.
def list_hurricane_settings_2 (HNS, GSS, TMS, CLHS):
	Hurricane_Settings = []
	for HN in HNS:
		for GS in GSS:
			for TM in TMS:
				for CLH in CLHS:
					Hurricane_Setting = HN + '_1Nest_2days_MainGrid' + GS + '_' + TM + '_vert42_' + CLH + '_cfl2p0'
					#print (Hurricane_Setting)
					Hurricane_Settings.append(Hurricane_Setting)
	return (Hurricane_Settings)
	#print (Hurricane_Settings)

def list_files_8(Dir):
	Post_Processed_Data = []
	for f in os.listdir(Dir):
		Post_Processed_Data.append(f)
	return (Post_Processed_Data)