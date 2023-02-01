# -*- coding: utf-8 -*-
# This is a post-processing python3 script that plots the 
#   1)volume conservasion
#   2)upper bounding 
#   3)lower bounding
from cProfile import label
import re
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Serif"
hfont = {'fontname':'Serif'}

quantityList = ["volumeFraction", "alphaMax", "alphaMin" ]
ylabelList=["|$V(t)$ - $V(0)$| / $V(0)$ [-]", r"max($\alpha$)(t)-1 [-]",r"-min($\alpha$)(t) [-]"]

applicationList = ["porousInterFoam", "porousInterIsoFoam"]

colorList=["r", "k", "b"]
nAlphaSubCyclesList = [0]

for i,quantity in enumerate(quantityList):
    fig, ax  =  plt.subplots()
    figureName = "porousDamBreak_general_comparison_"+quantity+".pdf"
    for j,application in enumerate(applicationList):
        if application == "porousInterIsoFoam":
            dataFile = "../"+application+"/porousDamBreak/logs/" + quantity +"_0"
            labelString = application 
            results = np.loadtxt(dataFile)
            if quantity == "volumeFraction":
                results[:,1] = abs(results[:,1]-results[0,1])/results[0,1]
            elif quantity == "alphaMax":
                results[:,1] = results[:,1]-1
            elif quantity == "alphaMin":
                results[:,1] = -results[:,1]
            
            ax.plot(results[:,0], results[:,1],"k",label = labelString)                                    
        else:
            dataFile = "../" + application+"/porousDamBreak/logs/" + quantity +"_0"
            labelString = application
            results = np.loadtxt(dataFile)
            if quantity == "volumeFraction":
                results[:,1] = abs(results[:,1]-results[0,1])/results[0,1]
                plt.ylim(top=1e-13)
                plt.ylim(bottom=1e-14)
            elif quantity == "alphaMax":
                plt.ylim(top=1e-9)
                plt.ylim(bottom=1e-11)
                results[:,1] = results[:,1]-1
            elif quantity == "alphaMin":
                results[:,1] = -results[:,1]
                plt.ylim(bottom=1e-70)
            ax.plot(results[:,0], results[:,1], "r", label = labelString)
    
    
    xLabel="$t$ [s]"
    yLabel=ylabelList[i]
    
    plt.xticks(fontsize = 24)
    plt.yticks(fontsize = 24)
    if quantity == "volumeFraction":
        plt.ylabel("normalized_"+yLabel,fontsize = 24)
    
    plt.yscale("log")
    plt.ylabel(yLabel,fontsize = 24,**hfont)
    
    plt.xlabel(xLabel,fontsize = 24,**hfont)

    plt.legend(loc="upper left",fontsize = 14)
    plt.grid()
    plt.tight_layout()
    
    
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)

    plt.locator_params(axis='x', nbins=6)

    plt.savefig(figureName)
