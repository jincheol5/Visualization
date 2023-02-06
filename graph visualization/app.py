import matplotlib.pyplot as plt
import numpy as np


y=['a','b','c','d','e']

x_list=[[1,2],[2,3],[3,4],[4,5]]


y_list=[['a','b'],['a','c'],['b','d'],['d','a']]


fig,ax_s=plt.subplots(ncols=4)

i=0
for ax in ax_s:
    ax.set_ylim(y)
    ax.plot(x_list[i],y_list[i])
    i+=1


fig.subplots_adjust(wspace=0)



plt.show()