import matplotlib
import matplotlib.colors as colors

# ----------------------------- Robot ------------------------------------------

ROBOT_OBJECTS_MAIN_BODY = 0

ROBOT_OBJECTS_UPPERLEG_BODY = 1
ROBOT_OBJECTS_UPPERLEG_BODY = 2
ROBOT_OBJECTS_UPPERLEG_BODY = 3
ROBOT_OBJECTS_UPPERLEG_BODY = 4

ROBOT_OBJECTS_LOWERLEG_BODY = 5
ROBOT_OBJECTS_LOWERLEG_BODY = 6
ROBOT_OBJECTS_LOWERLEG_BODY = 7
ROBOT_OBJECTS_LOWERLEG_BODY = 8

robotColors = {
ROBOT_OBJECTS_MAIN_BODY     : (0.0 , 0.0 , 0.0 ),

ROBOT_OBJECTS_UPPERLEG_BODY : (0.0 , 0.0 , 0.0 ),
ROBOT_OBJECTS_UPPERLEG_BODY : (0.0 , 0.0 , 0.0 ),
ROBOT_OBJECTS_UPPERLEG_BODY : (0.0 , 0.0 , 0.0 ),
ROBOT_OBJECTS_UPPERLEG_BODY : (0.0 , 0.0 , 0.0 ),

ROBOT_OBJECTS_LOWERLEG_BODY : (0.0 , 0.0 , 0.0 ),
ROBOT_OBJECTS_LOWERLEG_BODY : (0.0 , 0.0 , 0.0 ),
ROBOT_OBJECTS_LOWERLEG_BODY : (0.0 , 0.0 , 0.0 ),
ROBOT_OBJECTS_LOWERLEG_BODY : (0.0 , 0.0 , 0.0 )
}

# ------------------------------ Sensor data -----------------------------------

maximumDataRows    = 500
maximumDataColumns = 500

sensorDataValueMinimum = -1.0
sensorDataValueMaximum = +1.0

sensorDataRange = sensorDataValueMaximum - sensorDataValueMinimum

nameOfRawSensorData      = 's'
nameOfFinalFitnessValue  = 'f'

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

GnRd = colors.LinearSegmentedColormap('GnRd', cdict)

