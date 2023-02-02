import matplotlib.pyplot as plt

# create data
x=['t1','t2','t3','t4','t5']
y1=['a','b','c','d','e']


# make subplots
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4, sharey=False)
ax = (ax1,ax2,ax3,ax4)

# plot subplots and set xlimit
for i in range(4):
    ax[i].plot(x,y1,'g-.')
    ax[i].set_xlim([ x[i],x[i+1]])

# set width space to zero
plt.subplots_adjust(wspace=0)

# show plot
plt.show()