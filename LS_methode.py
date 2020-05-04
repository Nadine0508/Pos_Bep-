# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:06:14 2020

@author: Nadine Snijders 
"""

#LS formule om locatie te berekenen 

import numpy as np
import matplotlib.pyplot as plt

#Gemeten waarde tot punt 
D1 = 3.3
D2 = 4.6
D3 = 5.8
D4 = 6.5

# fixed point 
P1 = [-1,-2]
P2 = [-3,3]
P3 = [5,5]
P4 = [7,-1]

#formule 
A =  np.array([[P1[0]-P2[0],P1[1]-P2[1]] ,[P1[0]-P3[0],P1[1]-P3[1]] ,[P1[0]-P4[0],P1[1]-P4[1]]])
At = A.transpose()
Ax = At @ A 
An = np.linalg.inv(Ax)

b = np.array([[(P1[0]**2-P2[0]**2 + P1[1]**2-P2[1]**2 + D2**2 - D1**2) / 2],[(P1[0]**2-P3[0]**2 + P1[1]**2-P3[1]**2 + D3**2 - D1**2)/2],[(P1[0]**2-P4[0]**2 + P1[1]**2-P4[1]**2 + D4**2 - D1**2)/2]])

Pe = An @ At @ b 
print (Pe)

# plot circles and estimated position
C1 = plt.Circle((P1),D1,color = 'black',fill=False)
C2 = plt.Circle((P2),D2,color = 'black',fill=False)
C3 = plt.Circle((P3),D3,color = 'black',fill=False)
C4 = plt.Circle((P4),D4,color = 'black',fill=False)
C_loc = plt.Circle(Pe,0.1,color = 'red',fill=True)

fig, ax = plt.subplots()

ax.add_artist(C1)
ax.add_artist(C2)
ax.add_artist(C3)
ax.add_artist(C4)
ax.add_artist(C_loc)

ax.set_xlim((-10, 15))
ax.set_ylim((-10, 15))
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Least squares methode")
fig.savefig('plotcircles.png')
