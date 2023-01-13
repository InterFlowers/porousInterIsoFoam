# -*- coding: utf-8 -*-
#import
import re
import numpy as np
from matplotlib import pyplot as plt

plt.rc('text', usetex=True)  
plt.rc('font', family='Serif')  

#%% Functions
def regex_finder( fileName, upstreamStr, regexStr ):
#This function takes as an input three strings 
#fileName: Name of the file that you want to search for you expression 
#upstreamStr: A part of the line as a string in order to locate the correct lines 
#regexStr: The regular expression in a string of form 
#Output: It returns a list of values (valuesToFloats) that are found based on the regexStr 
    myFile=open(fileName)
    values=[]
    for line in myFile:  
       if upstreamStr in line:       
            print(line)
            x=re.search(regexStr, line )
            print(x)
            if x:
                values.append(float(x[0]))
        
    myFile.close()
    return values
#%% Main
file_path='../porousDamBreak/log.porousInterIsoFoam'
yValues_iso=regex_finder(file_path, 'volume fraction =', '(?<=volume fraction = )\d*\.*\d*e*\+*\-*\d*')
xValues_iso=regex_finder(file_path, 'Time = ', '(?<=Time = )\d*\.*\d*$')

#%% Plots  
figureName="porousDamBreak_total_volume_fraction_error_Co_0.5.pdf"
xLabel="Time [s]"
yLabel="(V-$V_{0}$)/$V_{0}$ [-]"

#normalize results
yValues_iso_norm=(yValues_iso-np.ones(len(yValues_iso))*(yValues_iso[0]))/np.ones(len(yValues_iso))/yValues_iso[0]

fig, ax = plt.subplots()
ax.plot(xValues_iso[:],abs(yValues_iso_norm[:]),'k')

plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.yscale("log")

plt.ylabel(yLabel,fontsize=24)
plt.xlabel(xLabel,fontsize=24)

plt.grid()
plt.tight_layout()

plt.savefig(figureName)

