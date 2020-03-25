import matplotlib.pyplot as plt

from fitnessFunction import FITNESS_FUNCTION

fitFn = FITNESS_FUNCTION()

fitFn.Draw()




for i in range(0,2):
    for j in range(0,2):

            axarr[i,j].set_xticks([0 + 0.5 , rows - 0.5])
            axarr[i,j].set_yticks([0 + 0.5 , cols - 0.5])

            axarr[i,j].set_xticklabels([0 , rows - 1])
            axarr[i,j].set_yticklabels([0 , cols - 1])

fig.tight_layout()
plt.show()
