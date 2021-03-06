import sys
sys.path.insert(0, '..')

import constants as c
import numpy as np
import pickle

class FITNESS_VARIABLE:

    def __init__(self,name):

        self.name = name

        if self.name == c.nameOfRawSensorData:

           self.data = pickle.load( open( "../sensorData/sensorData0.p", "rb" ) )

           self.rows , self.cols = self.data.shape

        elif self.name == c.nameOfFinalFitnessValue:

            self.rows    = 1
            self.cols    = 1

            self.data = np.random.random([self.cols,self.rows]) * c.sensorDataRange + c.sensorDataValueMinimum

        else:
            self.rows = np.random.randint(1,c.maximumDataRows)
            self.cols = np.random.randint(1,c.maximumDataColumns)

            self.data = np.random.random([self.cols,self.rows]) * c.sensorDataRange + c.sensorDataValueMinimum 

    def Assign_To_Panel(self,panelRow,panelColumn):

        self.panelRow    = panelRow

        self.panelColumn = panelColumn

    def Draw(self,fig,axis):

        self.Prepare_To_Draw(axis)

        im = axis[self.panelRow,self.panelColumn].pcolormesh(self.data,cmap=c.GnRd,vmin= c.sensorDataValueMinimum,vmax=c.sensorDataValueMaximum)

        self.Clean_Up_After_Drawing(fig,axis,im)

    def Get_Name(self):

        return self.name

# --------------- Private methods ---------------------------------

    def Clean_Up_After_Drawing(self,fig,axis,im):

        fig.colorbar(im , ax=axis[self.panelRow,self.panelColumn] , ticks = [-1,1] )

 
        if self.name == c.nameOfRawSensorData:

            self.Set_Ticks_For_Raw_Sensor_Data(axis)

        elif self.name == c.nameOfFinalFitnessValue:

            self.Set_Ticks_For_Final_Fitness_Value(axis)

        else:

            self.Set_Ticks(axis)

        if self.name == c.nameOfRawSensorData:

            self.Colorize_Y_Axis(axis)

    def Colorize_Y_Axis(self,axis):

        ticks = axis[self.panelRow,self.panelColumn].yaxis.get_ticklabels()

        robotSensorIndex = 0

        for tick in ticks:

            tick.set_color( c.robotColors[robotSensorIndex] )

            robotSensorIndex = robotSensorIndex + 1

    def Prepare_To_Draw(self,axis):

        axis[self.panelRow,self.panelColumn].axis('on')

        axis[self.panelRow,self.panelColumn].set_title(self.name)

    def Set_Ticks(self,axis):

        axis[self.panelRow,self.panelColumn].set_yticks([0 + 0.5 , self.rows - 0.5])
        axis[self.panelRow,self.panelColumn].set_xticks([0 + 0.5 , self.cols - 0.5])

        axis[self.panelRow,self.panelColumn].set_yticklabels([1 , self.rows])
        axis[self.panelRow,self.panelColumn].set_xticklabels([1 , self.cols])

    def Set_Ticks_For_Final_Fitness_Value(self,axis):

        axis[self.panelRow,self.panelColumn].set_yticks([0.5])
        axis[self.panelRow,self.panelColumn].set_xticks([0.5])

        axis[self.panelRow,self.panelColumn].set_yticklabels([1])
        axis[self.panelRow,self.panelColumn].set_xticklabels([1])

    def Set_Ticks_For_Raw_Sensor_Data(self,axis):

        axis[self.panelRow,self.panelColumn].set_yticks(       np.arange( 0 + 0.5 , self.rows + 0.5 ) )

        axis[self.panelRow,self.panelColumn].set_yticklabels(  np.arange( 0 + 1   , self.rows + 1   ) )


        axis[self.panelRow,self.panelColumn].set_xticks([0 + 0.5 , self.cols - 0.5])

        axis[self.panelRow,self.panelColumn].set_xticklabels( [1 , self.cols] )

       
        
