import sys
sys.path.insert(0, '..')
import constants as c

import sqlite3 as lite

class DATABASE:

    def __init__(self):

        self.Connect()

        if self.Not_Yet_Created():

            self.Create()

    def Add_User(self, userName):

        ID = self.Get_Next_Available_Record_ID_From_Table("Users")

        params = (ID, userName)

        self.Safe_Execute("INSERT INTO Users VALUES (?, ?)", params)

    def Get_Table_Records(self,tableName):

        executionString = "SELECT * FROM " + tableName

        self.Safe_Execute(executionString)

        return self.cur.fetchall()

    def User_Exists(self, userName):

        executionString = "SELECT * FROM Users WHERE Name=?"
        params = (userName,)
        self.Safe_Execute(executionString, params)
        users = self.cur.fetchall()

        return len(users) > 0

# -------------------- Private methods -------------------

    def Connect(self):

        self.con = lite.connect('../data/database.db')
        self.cur = self.con.cursor()

    def Create(self):

        self.Create_Tables()

    def Create_Tables(self):

        command = "CREATE TABLE " + c.DATABASE_USER_TABLE

        self.Safe_Execute(command)

    def Get_Next_Available_Record_ID_From_Table(self,tableName):

        executionString = "SELECT Id FROM " + tableName + " ORDER BY Id DESC LIMIT 1"
        self.Safe_Execute(executionString)
        ID = self.cur.fetchone()

        if not ID:
            return 0
        else:
            return int(ID[0]) + 1

    def Not_Yet_Created(self):

        self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' ''')

        numberOfTables = self.cur.fetchone()[0]

        return numberOfTables == 0

    def Safe_Execute(self,*args):

        self.cur.execute(*args)

        self.con.commit()
