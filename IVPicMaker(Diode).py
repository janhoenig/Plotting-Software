# -*- coding: utf-8 -*-
__author__ = 'cedric'

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1 import make_axes_locatable
from argparse import ArgumentParser
import configparser
import os
import matplotlib.font_manager
# print matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
# list = matplotlib.font_manager.get_fontconfig_fonts()
# names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in list]
# print names
# print matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf').find("FreeSerif")

parser = ArgumentParser(description='Oszi plotter')
parser.add_argument('-c','--filename', help='This program makes plots from oszi data!',\
                    default='D:/data/NitroStrip/NitroStrip24_07_17/IVLocations(Diode).txt')
args = parser.parse_args()

with open(args.filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]

#seperator = args.filename.rfind("/Mini")
#dataString = args.filename[0:seperator+1]

plt.rcParams['font.family']='Linux Libertine'
# plt.rcParams['font.family']='Liberation Serif'
plt.rcParams['font.size']=16
# plt.rcParams['font.libertine'] =['Linux Libertine']#['Times New Roman']
# plt.rc('font',family='Linux Libertine')
fig, ax = plt.subplots(figsize=(8,6))
i = 1
for file in content:
    startBin = 5000
    endBin = 6730
    timeOffset = 0.5
    seperator = file.rfind("/Waf")
    seperator2 = file.rfind("-run")
    nameString = file[seperator + 1:seperator2]
    seperator3 = file.rfind("-Diode")
    nameString2 = file[seperator + 1:seperator3]
    print(file)
    data = np.genfromtxt(file, delimiter=',', skip_header=0,
                         skip_footer=0, names=['volt', 'current'])


    for sep, item in enumerate(data['volt']):
        if abs(item) <= abs(data['volt'][sep-1]) and abs(item) > 0:
            break
    sep -= 1
    # fig, ax = plt.subplots(figsize=(16,12))

    #plt.rc('text', usetex=True)

    # ax.plot(data["time"][startBin:endBin]*1000000,data['Ch3'][startBin:endBin], label='Clear',linewidth=3)
    # ax.plot(data["time"][startBin:endBin]*1000000,data['Ch4'][startBin:endBin], label="Gate",linewidth=3)
    print(nameString2)
    if nameString2 == 'Waf2':
        ax.plot(data["volt"][0:sep],data['current'][0:sep]*1E6,color='black',linewidth=3)
    elif nameString2 == 'Waf8':
        ax.plot(data["volt"][0:sep],data['current'][0:sep]*1E6,color='red',linewidth=3)
    elif nameString2 == 'Waf14':
        ax.plot(data["volt"][0:sep], data['current'][0:sep] * 1E6, color='blue', linewidth=3)
    elif nameString2 == 'Waf20':
        ax.plot(data["volt"][0:sep], data['current'][0:sep] * 1E6, color='green', linewidth=3)
        print(sep)
        print(nameString)
    else:
        ax.plot(data["volt"], data['current'] * 1E6, color='brown', linewidth=3)
    i += 1
black = mpatches.Patch(color='black', label='FZ')
red_patch = mpatches.Patch(color='red', label='NIT')
blue = mpatches.Patch(color='blue', label='DOFZ')
green = mpatches.Patch(color='green', label='MCz')

ax.set_ylim(0,-0.5)
ax.set_xlim(0,-1000.0)

plt.xlabel(u"Voltage in V",fontsize=18)
plt.ylabel(u"Current in µA",fontsize=18)
# ax.plot(data['Ch2'], label="Gate",linewidth=3)
ax.grid(True)
# ticklines = ax.get_xticklines() + ax.get_yticklines()
# gridlines = ax.get_xgridlines() + ax.get_ygridlines()
# for line in gridlines:
#     line.set_linestyle('--')
# ax.legend(bbox_to_anchor=(0.6, 1.1), loc=2)
ax.legend(handles=[black,red_patch,blue,green])
# plt.show()
dataString = 'D:/data/NitroStrip/NitroStrip24_07_17'
fig.savefig(dataString+"/" + "IVCurves(Diode)"+".png")
fig.savefig(dataString+"/" + "IVCurves(Diode)"+".pdf")
# plt.show()
