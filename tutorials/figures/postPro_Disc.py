# -*- coding: utf-8 -*-
# This is a post-processing python3 script that plots the 
#   1)volume conservation
#   2)upper bounding 
#   3)lower bounding
from ast import If
from cProfile import label
import re
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
    

plt.rcParams["font.family"] = "Serif"
hfont = {'fontname':'Serif'}

quantityList = ["volumeFraction", "alphaMax", "alphaMin" ]
ylabelList=["|$V(t)$ - $V(0)$| / $V(0)$ [-]", r"max($\alpha$)(t)-1 [-]",r"-min($\alpha$)(t) [-]"]
yaxisLimit=[1e-13, 2e-4, 1e-10]
applicationList = ["porousInterFoam", "porousInterIsoFoam"]
colorList=["r","k"]

for i,quantity in enumerate(quantityList):
    fig, ax  =  plt.subplots()
    
    ax.axvline(0.25, 0, 1, c='gray',ls='--',linewidth=3)
    ax.axvline(2.3, 0, 1, c='gray',ls='--',linewidth=3)

    ax.axvline(0.75, 0, 1, c='gray',ls='-.',linewidth=3)
    ax.axvline(1.8, 0, 1, c='gray',ls='-.',linewidth=3)
    
    figureName = "discInConstantPorousFlow_general_comparison_"+quantity+".pdf"
    for j,application in enumerate(applicationList):
        dataFile = "../" + application + "/discInConstantPorousFlow/logs/" + quantity +"_0"
        labelString = application
        results = np.loadtxt(dataFile)
        if quantity == "volumeFraction":
            results[:,1] = abs(results[:,1]-results[0,1])/results[0,1]
        elif quantity == "alphaMax":
            results[:,1] = results[:,1]-1
                
        elif quantity == "alphaMin":
            results[:,1] = -results[:,1]
        if  quantity!="alphaMax":
            ax.plot(results[:,0], results[:,1], colorList[j],label = labelString)
        
        resultsMax1 = np.max(results[:,1])
        resultsMin1 = np.min(results[:,1])                                    
        

    
    xLabel="$t$ [s]"
    yLabel=ylabelList[i]
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)

    plt.xlabel(xLabel,fontsize = 24,**hfont)
    ax.set_ylabel(yLabel,fontsize = 24,**hfont)
    plt.yscale('log')
      
       

    plt.legend(loc="upper left",fontsize = 14)
    if i==2:     
        plt.legend(bbox_to_anchor=(0.0, 0.76), loc='upper left', borderaxespad=0, fontsize = 14)
    
    plt.grid()
    plt.tight_layout()

    if quantity=="volumeFraction":
        ax.set_yticks([1e-16, 1e-15, 1e-14])    
    
    if quantity=="alphaMax":
        plt.yscale("linear")
        application = "porousInterFoam"
        maxCo = 0.25
        
        dataFile = "../" + application + "/discInConstantPorousFlow/logs/" + quantity +"_0"
        x1=np.loadtxt(dataFile)
        x1[:,1] = x1[:,1] - 1
         
        color = 'r'
    
        application = "porousInterIsoFoam"
        maxCo = 0.25
        dataFile = "../" + application + "/discInConstantPorousFlow/logs/" + quantity +"_0"
        x2=np.loadtxt(dataFile)
        x2[:,1] = x2[:,1] - 1 
        
        fig, (ax1, ax2,) = plt.subplots(2, sharex=True)
        
        ax1.set_yscale("symlog")

        
        ax1.set_yticks([0.000000001,   -0.0000001],fontsize = 24)
        ax1.tick_params(axis='y', labelsize=24 )
        ax1.axvline(0.25, 0, 1, c='gray',ls='--',linewidth=3)
        ax1.axvline(2.3, 0, 1, c='gray',ls='--',linewidth=3)
        ax1.axvline(0.75, 0, 1, c='gray',ls='-.',linewidth=3)
        ax1.axvline(1.8, 0, 1, c='gray',ls='-.',linewidth=3)
        ax1.plot(x1[:,0], x1[:,1],"r", label = "porousInterFoam")
        ax1.legend(fontsize=14)
        ax1.grid("")

        
        ax2.set_yscale("log")
        ax2.set_yticks([0.000000000000001, 0.00000000000001,  0.0000000000001],fontsize = 24,**hfont)
        ax2.axvline(0.25, 0, 1, c='gray',ls='--',linewidth=3)
        ax2.axvline(2.3, 0, 1, c='gray',ls='--',linewidth=3)
        ax2.axvline(0.75, 0, 1, c='gray',ls='-.',linewidth=3)
        ax2.axvline(1.8, 0, 1, c='gray',ls='-.',linewidth=3)
        ax2.plot(x2[:,0], x2[:,1],"k",label = "porousInterIsoFoam")
        ax2.tick_params(axis='y', labelsize=24 )
        ax2.tick_params(axis='x', labelsize=24 )
        plt.xlabel(xLabel,fontsize = 24,**hfont)
        fig.text(0.001, 0.5, ylabelList[1], fontsize = 24, va='center', rotation='vertical',**hfont)   
        plt.tight_layout()
        fig.set_size_inches(7, 5.5)
        ax2.minorticks_off() 
        plt.legend(fontsize=14)

    plt.savefig(figureName)

