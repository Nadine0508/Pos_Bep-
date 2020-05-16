# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:02:40 2020

@author: Nadine Snijders 
"""

import numpy as np
import matplotlib.pyplot as plt

t_0 = 0
t_1 = 15
a = 20
bias = 2
drift = 0.02

v = []
x = []
ux = []
uy = []

ux_bias = []
uy_bias = []

ux_drift = []
uy_drift = []

ux_drift_bias = []
uy_drift_bias = []

for i in range (0,16,1):
    
    v.append(20 * i) 
    x.append( 20/2 * i**2)
    
    ux.append ((np.sqrt(3)/2) * ((a/2 * i**2)))
    uy.append ((1/2) * (( a/2 * i**2)))
    
    ux_bias.append((np.sqrt(3)/2) * (( (a + bias)/2 * i**2) ))
    uy_bias.append((1/2)* (( ( a + bias)/2 * i**2)))
    
    ux_drift.append((np.sqrt(3)/2) * (((a + (drift * i))/2 * i**2)))
    uy_drift.append((1/2)* (( ( a + (drift * i))/2 * i**2)))
    
    ux_drift_bias.append((np.sqrt(3)/2) * (((a + bias + (drift * i))/2 * i**2)))
    uy_drift_bias.append((1/2)* (( ( a + bias + (drift * i))/2 * i**2)))
    

print (ux[15],uy[15])
print (ux_bias[15],uy_bias[15])
print (ux_drift_bias[15],uy_drift_bias[15])

plt.plot (ux)
plt.plot (uy)

plt.plot (ux_bias)
plt.plot (uy_bias)

plt.plot (ux_drift_bias)
plt.plot (uy_drift_bias)

plt.show