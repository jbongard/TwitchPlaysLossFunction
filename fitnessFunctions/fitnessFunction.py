import math
import matplotlib.pyplot as plt
import numpy as np

from fitnessVariable import FITNESS_VARIABLE

class FITNESS_FUNCTION:

    def __init__(self):

        self.variables = {}

        self.Add_Variable('s')
        self.Add_Variable('f')

    def Add_Variable(self,variableName):

        variable = FITNESS_VARIABLE(variableName)

        self.variables[ variable.Get_Name() ] = variable 

    def Draw(self):

        self.Prepare_To_Draw()

        self.Assign_Variables_To_Panels()

        self.Hide_All_Unused_Panels()

        for variable in self.variables:

            self.variables[variable].Draw(self.fig,self.axarr)

        self.Clean_Up_After_Drawing()

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

    def Clean_Up_After_Drawing(self):

        self.fig.tight_layout()

        plt.show()

    def Hide_All_Unused_Panels(self):

        for i in range(self.numberOfRows):

            for j in range(self.numberOfColumns):

                self.axarr[i,j].axis('off')
 
    def Prepare_To_Draw(self):

        self.numberOfRows = math.ceil( math.sqrt( len(self.variables) ) )

        self.numberOfColumns = self.numberOfRows

        self.fig, self.axarr = plt.subplots(self.numberOfRows , self.numberOfColumns)

        self.fig.suptitle('Best bot so far.', fontsize=16)

