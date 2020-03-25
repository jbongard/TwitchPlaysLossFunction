import math
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

        self.Assign_Variables_To_Panels()

        for variable in self.variables:

            self.variables[variable].Draw(self.axarr)

        plt.show()

        exit()

    def Print(self):

        print(self.variables)

# ----------------------- Private functions ------------------------

    def Assign_Variables_To_Panels(self):

        row = 0
        column = 0

        for variable in self.variables:

            self.variables[variable].Assign_To_Panel(row,column)

            column = column + 1

            if column == self.numberOfColumns:

                column = 0
                row    = row + 1

    def Prepare_To_Draw(self):

        self.numberOfRows = math.ceil( math.sqrt( len(self.variables) ) )

        self.numberOfColumns = self.numberOfRows

        self.fig, self.axarr = plt.subplots(self.numberOfRows , self.numberOfColumns)

        self.fig.suptitle('Best bot so far.', fontsize=16)

