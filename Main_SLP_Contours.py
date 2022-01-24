from typing import Counter
from wrf import (getvar, interplevel, smooth2d, to_np, latlon_coords, get_cartopy, cartopy_xlim, cartopy_ylim)
from Func_Extract_Data import Extract_Track_Data
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import NaturalEarthFeature
from Func_List_Files import list_ncfiles
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from netCDF4 import Dataset
import cartopy.crs as crs
import numpy as np
import math
import os


Real_data_dir='/Users/lmatak/Desktop/leo_simulations/Real_Data'

# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "sans-serif",
#     "font.sans-serif": ["Helvetica"]})
# # for Palatino and other serif fonts use:
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.serif": ["Palatino"],
# })

# Define the hurricane's directory.
Input_Dir = '/Users/lmatak/Desktop/some_wrfout_files/'
# Choose between : 'Gustav', 'Irma', 'Katrina', 'Maria'
HNS = ['Dorian','Iota','Laura','Lorenzo']
# Choose between : '2km', '4km', '8km', '16km', '32km'
GSS = ['4km']
# Choose between : 'NoTurb', 'Smag2D', 'TKE2D'
TMS = ['NoTurb']
# Choose between : 'cLh0p2', 'cLh0p5', 'cLh1p0', 'cLh1p5'
PBLS=['YSU']
CLS = ['250','1.0','2000']
# Choose between: '0', '1', '2', '3', '4', '5'
Time_idx = 0
hn_counter=-1
cl_counter=0
# Choose the altitude:
Alt = 300
max_wspd=0
nbins=8
cmap_name='my_colors'
#coolwarm is the red-blue one
cmap=plt.get_cmap(
    'twilight_shifted')
# Create a figure
fig, ax = plt.subplots(nrows=4, ncols=3, figsize=(11,8), sharex=False, sharey='row',subplot_kw={'projection': crs.PlateCarree()})
plt.subplots_adjust(left=0.2, bottom=None, right=None, top=None, wspace=0, hspace=None)
# plt.subplots(constrained_layout=True)
figure_indices = np.array(['(a)', '(b)'])
colors=['lightyellow','indigo','lightgreen','lightblue','blue','yellow','red','black']
cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=nbins)
for HN in HNS:
    hn_counter+=1

    for GS in GSS:
        for TM in TMS:
            i = 0
            for PBL in PBLS:
                for CL in CLS: 
                    ncfiles = []                    
                    Hurricane_Setting = HN + '_' + GS + '_' + TM + '_' + PBL +'_hpbl_'+CL
                    Input_Dir_1 = Input_Dir +  Hurricane_Setting


                    ncfiles = list_ncfiles(Input_Dir_1, ncfiles)

                    for ncfile in ncfiles[0:1]:

                        # Set the working space.
                        os.chdir(Input_Dir_1)
                        # Open the NetCDF file
                        Data = Dataset(ncfile)

                        #Extract the necessary data to plot the contour map.
                        slp = getvar(Data, "slp", timeidx = Time_idx)
                        z = getvar(Data, "z", timeidx = Time_idx)
                        wspd = getvar(Data, "wspd", timeidx = Time_idx)

                        
                        # Download and add the states and coastlines
                        # states = NaturalEarthFeature(category="cultural", scale="50m",
                        #                              facecolor="none",
                        #                              name="admin_1_states_provinces_shp")
                        # ax[i].add_feature(states, linewidth=.5, edgecolor="black")
                       
                        ax[hn_counter,i].stock_img()
                        ax[hn_counter,i].coastlines('50m', linewidth=0.8)
                        gl = ax[hn_counter,i].gridlines(crs=crs.PlateCarree(), draw_labels=True,
                            linewidth=0.2, color='black', alpha=0.2, linestyle='--')
                        gl.top_labels = False
                        gl.right_labels = False
                        gl.xlabel_style= {'size': 12, 'color': 'black'}
                        gl.ylabel_style= {'size': 12, 'color': 'black'}

                        # Interpolate geopotential height, u, and v winds to 500 hPa
                        wspd_500 = interplevel(wspd, z, Alt)



                        # Get the latitude and longitude points
                        lats, lons = latlon_coords(wspd_500)

                        # Get the cartopy mapping object
                        cart_proj = get_cartopy(wspd_500)
                            #this is for wind speed
                            #lvls thinh is just how many nijansi boje
                        if (float(np.amax(wspd))) > max_wspd:
                            max_wspd=float(np.amax(wspd))
                            im_cbar = ax[hn_counter,i].contourf(to_np(lons), to_np(lats), to_np(wspd_500), 25,
                                transform=crs.PlateCarree(),vmin=0 ,vmax=max_wspd,
                                cmap= cmap)
                        else:
                            im = ax[hn_counter,i].contourf(to_np(lons), to_np(lats), to_np(wspd_500), 25,
                                transform=crs.PlateCarree(),vmin=0 ,vmax=max_wspd,
                                cmap= cmap)
                            #this is for SLP countours
                        CS = ax[hn_counter,i].contour(to_np(lons), to_np(lats), to_np(slp), 6, colors="black", alpha=1,
                            transform=crs.PlateCarree(), linewidths = 1)
                        # Real_Lats = []
                        # Real_Longs = []
                        # Real_Lats = Extract_Track_Data (Real_data_dir, Real_Lats, 'Lat',HN)
                        # Real_Longs = Extract_Track_Data (Real_data_dir, Real_Longs, 'Lon',HN)

                        if HN == 'Iota':
                            ax[hn_counter,i].set_extent([-79,-81, 13 , 15])
                            
                        elif HN =='Lorenzo':
                            ax[hn_counter,i].set_extent([-37,-39, 13.5 , 15.5])
                            
                        elif HN=='Dorian':
                            ax[hn_counter,i].set_extent([-69.75,-71.75, 24.5 , 26.5])
                            
                        elif HN=='Laura':
                            ax[hn_counter,i].set_extent([-88.5,-90.5, 25 , 27])
                            
                        # ax[i].set_extent([-70,-72, 24.5 , 26])
                        ax[hn_counter,i].clabel(CS, CS.levels, inline=True, fontsize=8, inline_spacing=8,  use_clabeltext=True)
                        
                        # ax[hn_counter,i].set_title(HN[0:2] + '-' + GS + '-' + PBL+ '-' + CL, {'size': 16}, pad= 1, y = 1.1)
                        # ax[i].annotate(figure_indices[i], xy=(-79, 27.5), xytext=(10, 340), textcoords='axes points',
                    # color='white', size='x-large')
                    print('i for ylabels:',i)
                    
                    i = i + 1




# ax[0,0].annotate('Dorian',
#             xy=(.08, .765), xycoords='figure fraction',
#             horizontalalignment='center', verticalalignment='baseline',rotation='vertical',
#             fontsize=20)
# ax[0,0].set_ylabel('ahain wat the fuck')

# Add a color bar
for i in range(len(CLS)):
    ax[0,i].set_title('HPBL - ' + CLS[i], {'size': 16})
for i in range(len(HNS)):
    
    ax[i,0].annotate(HNS[i],
    #first numver in xy=() is x-axis
            xy=(.16, .765-i/5), xycoords='figure fraction',
            horizontalalignment='center', verticalalignment='baseline',rotation='vertical',
            fontsize=20)
    # gl=ax[i,0].set_ylabel(HNS[i])
    # gl = ax[i,0].gridlines(crs=crs.PlateCarree(), draw_labels=True,
    #                         linewidth=0.2, color='black', alpha=0.2, linestyle='--')
    # gl.top_labels = False
    # gl.right_labels = False
    # gl.xlabel_style= False
    # gl.ylabel_style= False


# fig.subplots_adjust(right=0.8)


# fig.suptitle(HN+' - '+GS+' - '+TM+' - '+PBL+' - '+'wspd / slp @'+str(Alt), fontsize=18,y=0.8)
#first coord is the x-axis
cbar_ax = fig.add_axes([0.88, 0.15, 0.02, 0.7])

cbar = plt.colorbar(im_cbar, cax=cbar_ax)#, label = 'Wind Speed [m/s] at 500 m Above Sea-Level')
cbar.set_label('Wind Speed [m/s] at 300 m Above Sea-Level', rotation = 270, labelpad = 25, size = 'xx-large')
cbar.ax.tick_params(labelsize=12)

plt.show()
