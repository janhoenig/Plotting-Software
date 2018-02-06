# -*- coding: utf-8 -*-
__author__ = 'cedric'

import numpy as np
from matplotlib import pyplot as plt
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
                    default='D:/data/NitroStrip/NitroStrip/IVLocations.txt')
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
for file in content:
    startBin = 5000
    endBin = 6730
    timeOffset = 0.5
    seperator = file.rfind("/Mini")
    seperator2 = file.rfind("-run")
    nameString = file[seperator + 1:seperator2]
    print(file)
    data = np.genfromtxt(file, delimiter=',', skip_header=0,
                         skip_footer=0, names=['volt', 'current'])



    # fig, ax = plt.subplots(figsize=(16,12))

    #plt.rc('text', usetex=True)

    # ax.plot(data["time"][startBin:endBin]*1000000,data['Ch3'][startBin:endBin], label='Clear',linewidth=3)
    # ax.plot(data["time"][startBin:endBin]*1000000,data['Ch4'][startBin:endBin], label="Gate",linewidth=3)

    ax.plot(data["time"]/60,data['current']*1E6, label=nameString,linewidth=3,color='r')


ax.set_ylim(-0.1,-0.7)
#ax.set_xlim(0,-600.0)

plt.xlabel(u"Time in minutes",fontsize=18)
plt.ylabel(u"Current in µA",fontsize=18)
# ax.plot(data['Ch2'], label="Gate",linewidth=3)
ax.grid(True)
# ticklines = ax.get_xticklines() + ax.get_yticklines()
# gridlines = ax.get_xgridlines() + ax.get_ygridlines()
# for line in gridlines:
#     line.set_linestyle('--')
# ax.legend(bbox_to_anchor=(0.6, 1.1), loc=2)
ax.legend()
# plt.show()
dataString = 'D:/data/NitroStrip/NitroStrip'
fig.savefig(dataString+"/" + "IVCurves"+".png")
fig.savefig(dataString+"/" + "IVCurves"+".pdf")
# plt.show()
