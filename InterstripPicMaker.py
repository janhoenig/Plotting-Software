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
                    default='D:/data/NitroStrip/NitroStrip/InterstripLocations.txt')
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
fig, ax = plt.subplots(figsize=(7,8))
ax.set_xticks(np.arange(0,5,1))
ax.set_xticklabels(['FZ','NIT','DOFZ','MCz'], rotation='vertical', fontsize=18)
i = 1
for file in content:
    startBin = 5000
    endBin = 6730
    timeOffset = 0.5
    seperator = file.rfind("/Mini")
    seperator2 = file.rfind("-run")
    nameString = file[seperator + 1:seperator2]
    seperator3 = file.rfind("-pos")
    nameString2 = file[seperator + 1:seperator3]
    print(file)
    data = np.genfromtxt(file, delimiter=',', skip_header=0,
                         skip_footer=0)


    print(data.shape[0])
    if nameString2 == 'Mini2':
        itemindex = np.where(data[:, 0] == 250)
        ax.plot( 0 , data[itemindex, data.shape[1]-4]*1E12, marker = 'o',color='black', markersize= 10)
        print(data[itemindex,0])
        print(data[itemindex, data.shape[1]-4])
    elif nameString2 == 'Mini8':
        itemindex = np.where(data[:, 0] == 300)
        ax.plot( 1 , data[itemindex, data.shape[1] - 4]*1E12, marker='o', color='red', markersize=10)
        print(data[itemindex, 0])
        print(data[itemindex, data.shape[1] - 4])
    elif nameString2 == 'Mini14':
        itemindex = np.where(data[:, 0] == 150)
        ax.plot( 2 , data[itemindex, data.shape[1] - 4]*1E12, marker='o', color='blue', markersize=10)
    elif nameString2 == 'Mini20':
        itemindex = np.where(data[:, 0] == 300)
        ax.plot( 3 , data[itemindex, data.shape[1] - 4]*1E12, marker='o', color='green', markersize=10)
        print(data[itemindex, 0])
        print(data[itemindex, data.shape[1] - 4])
    else:
        ax.plot(data[0], 1.0/(data[:,2]*data[:,2]), color='brown', linewidth=3)
    i += 1
black = mpatches.Patch(color='black', label=u'FZ @ 250V')
red_patch = mpatches.Patch(color='red', label='NIT @ 300V')
blue = mpatches.Patch(color='blue', label='DOFZ @ 150V')
green = mpatches.Patch(color='green', label='MCz @ 300V')
#ax.set_yscale('log')

ax.set_ylim(0,4)
ax.set_xlim(-0.5,3.5)

#plt.xlabel(u"Voltage in V",fontsize=18)
plt.ylabel(u"Capacitance in pF",fontsize=18)
# ax.plot(data['Ch2'], label="Gate",linewidth=3)
ax.grid(True)
# ticklines = ax.get_xticklines() + ax.get_yticklines()
# gridlines = ax.get_xgridlines() + ax.get_ygridlines()
# for line in gridlines:
#     line.set_linestyle('--')
# ax.legend(bbox_to_anchor=(0.6, 1.1), loc=2)
ax.legend(handles=[black,red_patch,blue,green])
make_axes_locatable(ax)
# plt.show()
dataString = 'D:/data/NitroStrip/NitroStrip'
fig.savefig(dataString+"/" + "Interstrip"+".png")
fig.savefig(dataString+"/" + "Interstrip"+".pdf")
# plt.show()
