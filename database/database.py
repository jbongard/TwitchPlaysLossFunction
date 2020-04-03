import sqlite3 as lite

class DATABASE:

    def __init__(self):

        self.Connect()

    def Reset(self):

        self.Destroy()
        self.Create()

# -------------------- Private methods -------------------

    def Connect(self):

        self.con = lite.connect('../data/database.db')
        self.cur = self.con.cursor()

    def Create(self):

        pass

    def Destroy(self):

        pass

        # self.Drop_Tables()

    def Drop_Tables(self):

        pass

        # self.Drop_Table("BuyRequests")

