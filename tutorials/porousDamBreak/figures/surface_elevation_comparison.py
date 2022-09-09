import re
import numpy as np
import math 
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
#plt.rc('text', usetex=True)  
#plt.rc('font', family='Serif',size=10)
plt.rcParams["font.family"] = "Serif"
fig, ax = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(10, 5))

for i in range(4,22,2):
    
    #%%Read files  
    experimental_data=np.loadtxt('experimentalData/data_'+str(i)+'.dat')
    #numerical_data_wave_mules=np.loadtxt('numericalData/freeSurface_wave_mules'+str(i)+'.dat')
    if (i%10==0):
        folderName=str(int(i*10/100))
    else:
        folderName=str((i*10/100))
    
    numerical_data_mules=np.loadtxt('../RESULTS_porousInterFoam_mesh3_Co_0.3/postProcessing/freeSurface/'+folderName+'/freeSurface.raw')
    numerical_data_mules_sorted = numerical_data_mules[np.argsort(numerical_data_mules[:, 0])]
    numerical_data_iso=np.loadtxt('../RESULTS_porousInterIsoFoam_mesh3_Co_0.3_isoAlpha_nAlphaSubCycles_0/postProcessing/freeSurface/'+folderName+'/freeSurface.raw')
    numerical_data_iso_sorted = numerical_data_iso[np.argsort(numerical_data_iso[:, 0])]
    numerical_data_iso2=np.loadtxt('../RESULTS_porousInterIsoFoam_mesh3_Co_0.3_plicRDF_nAlphaSubCycles_0/postProcessing/freeSurface/'+folderName+'/freeSurface.raw')
    numerical_data_iso_sorted2 = numerical_data_iso2[np.argsort(numerical_data_iso2[:, 0])]
    #%%Plot 
    figureName='surface_elevation_profiles.pdf'
    ax = plt.subplot(3,3,-1+int(i/2))
    ax.plot(experimental_data[:,0],experimental_data[:,1],'go', fillstyle='full', markersize=3,label="Liu et al. (1999)")
    ax.plot(numerical_data_mules_sorted[::1,0],numerical_data_mules_sorted[::1,1],'r', fillstyle='full',markersize=3,label="porousInterFoam")
    ax.plot(numerical_data_iso_sorted[::1,0],numerical_data_iso_sorted[::1,1],'k--',fillstyle='full',markersize=3,label="porousInterIsoFoam")
    #ax.plot(numerical_data_iso_sorted[::1,0],numerical_data_iso_sorted[::1,1],'b--',fillstyle='full',markersize=3,label="porousInterIsoFoamPLIC")
    plt.ylim(0,0.25)
    
    plt.grid(color='black',linestyle='--', linewidth=0.5)
    ax.add_patch(Rectangle((0.3,0),0.29,0.25,
                 edgecolor = 'black',
                 facecolor = 'silver',
                 fill=True,
                 lw=1))
    plt.text(0.005, 0.01, "t = "+str(i/10)+" s")
    
    if i not in list([16,18,20]):
        plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=True,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
   
    if i not in list([4, 10, 16]):
        plt.tick_params(
        axis='y',          
        which='both',      
        left=True,      
        right=False,        
        labelleft=False) 
    
    
    if i==8 :
        ax.legend(bbox_to_anchor =(0.5, 1.5),ncol=3)

xLabel="Horizontal position x [m] "
yLabel="Free surface elevation $\eta$ [m]"

fig.text(0.5, 0.008, xLabel, ha='center')
fig.text(0.04, 0.5, yLabel, va='center', rotation='vertical')
    
#plt.show()
plt.savefig(figureName)

   