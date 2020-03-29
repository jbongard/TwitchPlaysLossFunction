import sys
sys.path.insert(0, '..')

import constants as c
import numpy as np
import pickle

class ROBOT:

    def __init__(self):

        pass

    def Write_Sensor_Data(self):

        sensorData = np.random.random([ c.robotNumSensors , 1000 ]) * 2 - 1

        pickle.dump(  sensorData , open( "../sensorData/sensorData0.p", "wb" ) )

