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


parser = ArgumentParser(description='Oszi plotter')
parser.add_argument('-c','--filename', help='This program makes plots from oszi data!',\
                    default='D:/data/NitroStrip/Sensoren/IVLocations1e14.txt')
args = parser.parse_args()

with open(args.filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]



plt.rcParams['font.family']='Linux Libertine'

plt.rcParams['font.size']=16

fig, ax = plt.subplots(figsize=(8,6))
i = 1
for file in content:

    seperator = file.rfind("/Mini")
    seperator2 = file.rfind("-run")

    nameString = file[seperator + 1:seperator2]
    seperator3 = file.rfind("-pos")
    nameString2 = file[seperator + 1:seperator3]

    seperator = file.rfind("/Waf")
    seperator3 = file.rfind("-Strip")
    nameStringNew = file[seperator + 1:seperator3]

    seperator = file.rfind("/IV-Cold-")+8
    seperator3 = file.rfind("-Pos")
    nameStringIrrad = file[seperator + 1:seperator3]

    print(file)
    data = np.genfromtxt(file, delimiter=',', skip_header=0,
                         skip_footer=0, names=['volt', 'current'])


    for sep, item in enumerate(data['volt']):
        if abs(item) <= abs(data['volt'][sep-1]) and abs(item) > 0:
            break
    sep -= 1



    if nameString2 == 'Mini2' or nameStringNew == 'Waf2' or nameStringIrrad == 'FZ-Waver2':
        ax.plot( abs( data["volt"][0:sep] ), abs( data['current'][0:sep]*1E6 ),color='black',linewidth=3)
    elif nameString2 == 'Mini8'or nameStringNew == 'Waf8' or nameStringIrrad == 'NIT-Waver8':
        ax.plot( abs( data["volt"][0:sep] ), abs( data['current'][0:sep]*1E6 ),color='red',linewidth=3)
    elif nameString2 == 'Mini14'or nameStringNew == 'Waf14' or nameStringIrrad == 'DOFZ-Waver14':
        ax.plot( abs( data["volt"][0:sep] ), abs( data['current'][0:sep] * 1E6 ), color='blue', linewidth=3)
    elif nameString2 == 'Mini20'or nameStringNew == 'Waf20' or nameStringIrrad == 'MCZ-Waver20':
        ax.plot( abs( data["volt"][0:sep] ), abs( data['current'][0:sep] * 1E6 ) , color='green', linewidth=3)

    else:
        ax.plot(data["volt"], data['current'] * 1E6, color='brown', linewidth=3)

    i += 1
black = mpatches.Patch(color='black', label='FZ')
red_patch = mpatches.Patch(color='red', label='NIT')
blue = mpatches.Patch(color='blue', label='DOFZ')
green = mpatches.Patch(color='green', label='MCz')

#ax.set_ylim(0,-1.0)
#ax.set_xlim(0,-1000.0)

plt.xlabel(u"Voltage in V",fontsize=18)
plt.ylabel(u"Current in µA",fontsize=18)
# ax.plot(data['Ch2'], label="Gate",linewidth=3)
ax.grid(True)

ax.legend(handles=[black,red_patch,blue,green])
seperator = args.filename.rfind("IVLocations")+10
seperator3 = args.filename.rfind(".txt")
nameStringIrrad = args.filename[seperator + 1:seperator3]
print(nameStringIrrad)
ax.set_title("Fluence "+nameStringIrrad)
# plt.show()
dataString = 'D:/data/NitroStrip/Sensoren'
fig.savefig(dataString+"/" + "IVCurvesIrrad"+nameStringIrrad+".png")
fig.savefig(dataString+"/" + "IVCurvesIrrad"+nameStringIrrad+".pdf")
# plt.show()
