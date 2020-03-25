import constants as c
import numpy as np

class FITNESS_VARIABLE:

    def __init__(self,name):

        self.name = name

        self.cols = np.random.randint(1,500)
        self.rows = np.random.randint(1,500)

        self.data = np.random.random([self.cols,self.rows]) * 2 - 1

    def Assign_To_Panel(self,row,column):

        self.row    = row

        self.column = column

    def Draw(self,axis):

        axis[self.row,self.column].set_title(self.name)

        im = axis[self.row,self.column].pcolormesh(self.data,cmap=c.GnRd,vmin=-1,vmax=1)

        
    def Get_Name(self):

        return self.name
