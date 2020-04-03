import sys
sys.path.insert(0, '..')
import constants as c

from database import DATABASE

db = DATABASE()

print(c.DATABASE_USER_TABLE)

records = db.Get_Table_Records('Users')

print(records)
