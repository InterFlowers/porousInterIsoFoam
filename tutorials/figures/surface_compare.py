import re
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
#plt.rc('text', usetex=True)
#plt.rc('font', family='Serif')

fig, ax = plt.subplots(nrows=6, ncols=2, sharex=True, sharey=True, figsize=(5, 8))

for i in range(4,23,2):

    #%%Read files
    experimental_data=np.loadtxt('../porousDamBreak/experimentalData/data_'+str(i)+'.dat')
    if (i%10==0):
        folderName=str(int(i*10/100))
    else:
        folderName=str((i*10/100))

    numerical_data_iso=np.loadtxt('../porousDamBreak/postProcessing/freeSurface/'+folderName+'/freeSurface.raw')

    numerical_data_iso_sorted = numerical_data_iso[np.argsort(numerical_data_iso[:, 0])]
    #%%Plot
    figureName='InterfaceElevation.pdf'
    ax = plt.subplot(5,2,-1+int(i/2))
    ax.plot(experimental_data[:,0],experimental_data[:,1],'ko', mfc='none', markersize=3,label="Exp")
    ax.plot(numerical_data_iso_sorted[:,0],numerical_data_iso_sorted[:,1],'r', mfc='none',markersize=3,label="Numerical")
    plt.ylim(0,0.25)

    plt.grid(color='black',linestyle='--', linewidth=0.5)
    ax.add_patch(Rectangle((0.3,0),0.29,0.25,
                 edgecolor = 'black',
                 facecolor = 'gray',
                 fill=True,
                 lw=1))
    plt.text(0.005, 0.01, "t = "+str(i/10)+" s")

    if i not in list([20,22]):
        plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=True,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off

    if i%4 not in list([0]):
        plt.tick_params(
        axis='y',
        which='both',
        left=True,
        right=False,
        labelleft=False)


    if i==6:
        ax.legend()
xLabel="Horizontal position x [m] "
yLabel="Free surface elevation $\eta$ [m]"

fig.text(0.5, 0.08, xLabel, ha='center')
fig.text(0.03, 0.5, yLabel, va='center', rotation='vertical')

plt.show()
plt.savefig(figureName)

   
