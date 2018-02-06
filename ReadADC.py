import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1 import make_axes_locatable
from argparse import ArgumentParser
import configparser
import os


parser = ArgumentParser(description='Oszi plotter')
parser.add_argument('-c','--filename', help='This program makes plots from oszi data!',\
                    default='D:/PythonPrograms/analysis_556_to_1168.txt')
args = parser.parse_args()

with open(args.filename) as f:
    content = f.readlines()

#content = [x.strip() for x in content]

print(content)

listADC = []
listADCErr = []

listADCStr = []
listADCErrStr = []

a = np.array(content[6])
print(content[6].split())

for index in range(6,len(content),2):
    temp = content[index].split()
    listADC.append(float(temp[0]))
    listADCErr.append(float(temp[1]))
    listADCStr.append(temp[0])
    listADCErrStr.append(temp[1])


print(','.join(listADCStr[len(listADCStr)-11:len(listADCStr)-1]))
print(','.join(listADCErrStr[len(listADCStr)-11:len(listADCStr)-1]))
