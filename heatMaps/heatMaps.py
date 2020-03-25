import matplotlib.pyplot as plt

from fitnessFunction import FITNESS_FUNCTION

fitFn = FITNESS_FUNCTION()

fitFn.Draw()




for i in range(0,2):
    for j in range(0,2):

        axarr[i,j].set_xticks([0,rows-1])
        axarr[i,j].set_yticks([0,cols-1])

        fig.colorbar(im,ax=axarr[i,j])

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
