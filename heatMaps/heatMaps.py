import numpy as np
import matplotlib
import matplotlib.colors as colors
import matplotlib.pyplot as plt

# This dictionary defines the colormap
cdict = {'red':  ((0.0, 0.0, 0.0),   # no red at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.8, 0.8)),  # set to 0.8 so its not too bright at 1

        'green': ((0.0, 0.8, 0.8),   # set to 0.8 so its not too bright at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0)),  # no green at 1

        'blue':  ((0.0, 0.0, 0.0),   # no blue at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0))   # no blue at 1
       }

# Create the colormap using the dictionary
GnRd = colors.LinearSegmentedColormap('GnRd', cdict)


fig, axarr = plt.subplots(2,2)

fig.suptitle('Best bot so far.', fontsize=16)

for i in range(0,2):
    for j in range(0,2):

        if i==1 and j==1:

            cols = 1
            rows = 1
        else: 
            cols = np.random.randint(1,100)
            rows = np.random.randint(1,100)

        sensorData = np.random.random([cols,rows]) * 2 - 1
        
        im = axarr[i,j].pcolormesh(sensorData,cmap=GnRd,vmin=-1,vmax=1)

        axarr[i,j].set_xticks([0,rows-1])
        axarr[i,j].set_yticks([0,cols-1])

        fig.colorbar(im,ax=axarr[i,j])

        if i==0 and j==0: # First panel

            axarr[i,j].set_title('s')
        else:
            axarr[i,j].set_title('a = s')

        axarr[i,j].set_xticks([0,rows-1])
        axarr[i,j].set_yticks([0,cols-1])

        if i==1 and j==1: # last panel
       
            axarr[i,j].set_xticks([0.5])
            axarr[i,j].set_yticks([0.5])

            axarr[i,j].set_xticklabels([0])
            axarr[i,j].set_yticklabels([0])

        else:
            axarr[i,j].set_xticks([0 + 0.5 , rows - 0.5])
            axarr[i,j].set_yticks([0 + 0.5 , cols - 0.5])

            axarr[i,j].set_xticklabels([0 , rows - 1])
            axarr[i,j].set_yticklabels([0 , cols - 1])

fig.tight_layout()
plt.show()
