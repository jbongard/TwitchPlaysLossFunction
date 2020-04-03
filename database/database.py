import sys
sys.path.insert(0, '..')
import constants as c

import sqlite3 as lite

class DATABASE:

    def __init__(self):

        self.Connect()

        if self.Not_Yet_Created():

            self.Create()

    def Get_Table_Records(self,tableName):

        executionString = "SELECT * FROM " + tableName

        self.Safe_Execute(executionString)

        return self.cur.fetchall()

# -------------------- Private methods -------------------

    def Connect(self):

        self.con = lite.connect('../data/database.db')
        self.cur = self.con.cursor()

    def Create(self):

        self.Create_Tables()

    def Create_Tables(self):

        command = "CREATE TABLE " + c.DATABASE_USER_TABLE

        self.Safe_Execute(command)

    def Not_Yet_Created(self):

        self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' ''')

        numberOfTables = self.cur.fetchone()[0]

        return numberOfTables == 0

    def Safe_Execute(self,executionString):

        self.cur.execute(executionString)

        self.con.commit()
