import sys
from datetime import datetime
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# import camelcase


xpoints = np.array([0,5,6,9,20, 9,50,10,7])
ypoints = np.array([0,10, 20, 8,6, 30 ,23,15, 40])

# graph = plt.plot(ypoints, marker="D")
# plt.title("Uv index")
# plt.show()

# # the itterval lines are dotted 
# graph = plt.plot(ypoints, "D-.b", ms = 6) 
# plt.title("Uv index")
# plt.show()

# the itterval lines are dotted 
graph = plt.plot(xpoints, ypoints, color = "#ab1465", linewidth = "2")

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.xlabel("Uv index")
plt.ylabel("Time of day")
plt.title("UV degree", fontdict= font1, loc="left")
plt.show()