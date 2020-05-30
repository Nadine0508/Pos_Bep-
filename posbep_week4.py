# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:20:34 2020

@author: Nadine snijders
"""
import numpy as np
import matplotlib.pylab as plt 
fig, (ax1, ax2) = plt.subplots(2)
fig, (ax3, ax4, ax7) = plt.subplots(3)
fig, (ax5, ax6, ax8) = plt.subplots(3)

PRN1 = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
PRN2 = [1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1]

S1 = [19.1879, 11.7240, 12.5762, 3.1264, 18.8940, 9.4583, 4.3191, 18.8927, 16.0143, 18.5322, 5.9840, 14.1377, 13.9499, 2.5791, 8.5537, 15.0310, 24.3001, 15.2011, 28.0702, 26.6082, -1.0594, 1.2060, 5.3409, 8.2717, 3.5522, 21.3195, 16.0969, 18.8349, 24.2397, 27.8225, 5.8880, -8.8591, 4.9203, -0.0413, -0.0558, 11.7078, 26.3583, 16.0720, 14.4208, 16.4470, -1.3605, 2.2276, 2.5503, -0.9377, -0.8893, 20.0727, 23.0581, 29.2192, 24.4193, 17.6517, 8.2193, -6.4289, -7.9802, -7.4808,-5.8081]
S2 = [12.6446, 11.7673, 0.4556, 21.0563, 3.7195, 5.7141, 24.6145, 47.0135, 24.4946, 35.7627, 25.3772, 35.0881, 6.6029, 26.3966, 3.2701, 32.6804, -10.7296, 48.1218, -10.9793, 30.5112, 18.7386, 28.8869, 10.4255, 45.4270, 21.0632, 49.8134, -6.0594, 23.5847, 21.5168, 36.6411, 6.1498, 37.3996, 18.4575, 34.2437, -5.6191, 31.2018, 3.1885, 51.1761, 10.6821, 40.6202, 14.5864, 27.0289, 6.6626, 35.2111, -7.3967, 35.4202, 13.5973, 16.6318, 32.6145, 28.5241, 14.0412, 17.7143, 15.0692, 30.2466, 28.6366]

S3 = [31.8325, 23.4913, 13.0318, 24.1827, 22.6135, 15.1723, 28.9336, 65.9062, 40.5089, 54.2949, 31.3611, 49.2259, 20.5528, 28.9757, 11.8238, 47.7115, 13.5705, 63.3229, 17.0909, 57.1194, 17.6791, 30.0928, 15.7664, 53.6987, 24.6154, 71.1328, 10.0375, 42.4196, 45.7565, 64.4636, 12.0377, 28.5404, 23.3778, 34.2024, -5.6748, 42.9096, 29.5468, 67.2480, 25.1029, 57.0672, 13.2260, 29.2565, 9.2129, 34.2734, -8.2859, 55.4929, 36.6555, 45.8510, 57.0339, 46.1758, 22.2605, 11.2854, 7.0890, 22.7658, 22.8284];

ax8.plot (PRN1,drawstyle='steps-pre')
ax7.plot (PRN2,drawstyle='steps-pre')

ax3.acorr(S1)
ax5.acorr(S2)
data = ax2.acorr(S3)[1]

auto_PRN1 = []
auto_PRN2 = []
abs3      = []

for i in range (0,len(PRN1),1):
    auto_PRN1.append((1/len(PRN1))* PRN1[i] * (PRN1[i] + i))   
ax6.acorr(auto_PRN1)

for i in range (0,len(PRN2),1):
    auto_PRN2.append((1/len(PRN2))* PRN2[i] * (PRN2[i] + i)) 
ax4.acorr(auto_PRN2)
    
for i in range (0,len((data)),1):
    if data[i] > 0.68:
        abs3.append (1)
    else:
        abs3.append (-1)
       
ax1.plot(abs3,drawstyle='steps-pre')
