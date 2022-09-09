#%%Include
from ast import For
from cProfile import label
import re
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)

#%%Initialize

xc = 0.5
yc = 0.5
r = .25

th = 2*np.pi*np.arange(0, 1, 0.005)
x = xc + r*np.cos(th)
y = yc + r*np.sin(th)
z = np.zeros(np.size(th))

dt = 0.01
tEnd = 2.5
nSteps = tEnd/dt
tarray = np.arange(0, tEnd,dt)

ux = 1
uy = 0.5
porosity = 0.5

xleft = 1
xright = 4
# Open a file to write


np.savetxt("discThroughPorousMaterialPositions"+ str(tarray[0]),(np.c_[x,y,z]))
#%% Iterate and plot
for n in range(np.size(tarray)):
    
    
    ind = np.where((x[:] > xleft) & (x[:] < xright))
    Ux = ux*np.ones(np.size(x))
    Uy = uy*np.ones(np.size(y))
    
    Ux[ind] = Ux[ind]/porosity
    Uy[ind] = Uy[ind]/porosity
    
    
    x = x + dt*Ux
    y = y + dt*Uy

    plt.plot(x,y,'.-')
    plt.grid()
    plt.show()
    
    # f = open("discThroughPorousMaterialPositions" + str(tarray[n]) + ".dat", "a")
    if tarray[n] in [0.49, 0.99, 1.49, 1.99, 2.49]:
        np.savetxt("discThroughPorousMaterialPositions"+ str(tarray[n]),(np.c_[x,y,z]))
    # f.write(x + "\t" + y + "\t")
    # f.close()