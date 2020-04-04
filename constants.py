import matplotlib
import matplotlib.colors as colors

# -------------------------- Database ------------------------------------------

DATABASE_USER_TABLE          = "Users(Id INT, Name TEXT)"

# ----------------------------- Robot ------------------------------------------

ROBOT_OBJECTS_MAIN_BODY      = 0

ROBOT_OBJECTS_UPPERLEG_LEFT  = 1
ROBOT_OBJECTS_UPPERLEG_RIGHT = 2
ROBOT_OBJECTS_UPPERLEG_FRONT = 3
ROBOT_OBJECTS_UPPERLEG_BACK  = 4

ROBOT_OBJECTS_LOWERLEG_LEFT  = 5
ROBOT_OBJECTS_LOWERLEG_RIGHT = 6
ROBOT_OBJECTS_LOWERLEG_FRONT = 7
ROBOT_OBJECTS_LOWERLEG_BACK  = 8

robotColors = {

ROBOT_OBJECTS_MAIN_BODY      : (0.0 , 0.0 , 0.0 ),

ROBOT_OBJECTS_UPPERLEG_LEFT  : (1.0  , 0.0 , 0.0 ),
ROBOT_OBJECTS_UPPERLEG_RIGHT : (0.8 , 0.0 , 0.0 ),
ROBOT_OBJECTS_UPPERLEG_FRONT : (0.6  , 0.0 , 0.0 ),
ROBOT_OBJECTS_UPPERLEG_BACK  : (0.4 , 0.0 , 0.0 ),

ROBOT_OBJECTS_LOWERLEG_LEFT  : (0.0 , 1.0 , 0.0 ),
ROBOT_OBJECTS_LOWERLEG_RIGHT : (0.0 , 0.8 , 0.0 ),
ROBOT_OBJECTS_LOWERLEG_FRONT : (0.0 , 0.6 , 0.0 ),
ROBOT_OBJECTS_LOWERLEG_BACK  : (0.0 , 0.4 , 0.0 )
}

robotNumSensors = len( robotColors )

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

