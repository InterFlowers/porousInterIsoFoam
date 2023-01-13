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
file_path='../discInConstantPorousFlow/log.porousInterIsoFoam'
y=regex_finder(file_path,'min(alpha', '(?<=min\(alpha\) = )\+*\-*\d*\.*\d*e*\+*\-*\d*')
x=regex_finder(file_path, 'Time = ', '(?<=Time = )\d*\.*\d*$')

#%% Plots  
figureName="discInConstantPorousFlow_lower_bounding_Co_0.5.pdf"
xLabel="Time [s]"
yLabel="abs(min(alpha)) [-]"
#replace all values with mag less than 1e-25 with 0  
for i in np.arange(len(y)):
    if(y[i]<1e-25 and y[i]>-1e-25):
        y[i]=0
        

fig, ax = plt.subplots()
ax.plot(x[:],np.abs(y[:]),'k')

#plot vertical dashed lines
ax.axvline(0.25, 0, 1, c='k',ls='--')
ax.axvline(2.3, 0, 1, c='k',ls='--')

ax.axvline(0.75, 0, 1, c='k',ls='-.')
ax.axvline(1.8, 0, 1, c='k',ls='-.')

plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.yscale("log")

plt.ylabel(yLabel,fontsize=24)
plt.xlabel(xLabel,fontsize=24)

plt.grid()
plt.tight_layout()
plt.savefig(figureName)
