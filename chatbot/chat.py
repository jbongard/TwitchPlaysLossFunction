class CHAT:

    def __init__(self,db,userName,chatString):

        self.db         = db

        self.userName   = userName

        self.chatString = chatString

    def Process(self):

        self.Handle_Returning_User()

        self.Handle_New_User()

# ----------------- Private methods ---------------------

    def Handle_New_User(self):

        if not self.db.User_Exists(self.userName):

            self.db.Add_User(self.userName)

            print('Welcome!')
       
    def Handle_Returning_User(self):

        if self.db.User_Exists(self.userName):

            pass

