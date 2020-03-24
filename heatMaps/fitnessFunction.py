import math
import matplotlib
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np

from fitnessVariable import FITNESS_VARIABLE

class FITNESS_FUNCTION:

    def __init__(self):

        self.variables = {}

        self.Add_Variable('s')
        self.Add_Variable('a')
        self.Add_Variable('b')
        self.Add_Variable('c')

    def Add_Variable(self,variableName):

        variable = FITNESS_VARIABLE(variableName)

        self.variables[ variable.Get_Name() ] = variable 

    def Draw(self):

        self.Prepare_To_Draw()

        for variable in self.variables:

            self.variables[variable].Draw(self.axarr)

        plt.show()

        exit()

    def Print(self):

        print(self.variables)

# ----------------------- Private functions ------------------------

    def Prepare_To_Draw(self):

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

        numberOfRows = math.ceil( math.sqrt( len(self.variables) ) )

        numberOfColumns = numberOfRows

        self.fig, self.axarr = plt.subplots(numberOfRows , numberOfColumns)

        self.fig.suptitle('Best bot so far.', fontsize=16)

