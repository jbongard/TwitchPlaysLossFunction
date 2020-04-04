class CHAT:

    def __init__(self,db,userName,chatString):

        self.db         = db

        self.userName   = userName

        self.chatString = chatString

    def Process(self):

        if self.New_User():

            self.Handle_New_User()

        self.db.Add_Chat(self.chatString,self.userName)

# ----------------- Private methods ---------------------

    def Handle_New_User(self):

        self.db.Add_User(self.userName)

        print('Welcome!')
       
    def Handle_Returning_User(self):

        pass

    def New_User(self):

        return not self.db.User_Exists(self.userName)
