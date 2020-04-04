import sys
sys.path.insert(0, '..')
import constants as c

from database import DATABASE

db = DATABASE()

db.Print()

