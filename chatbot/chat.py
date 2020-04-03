class CHAT:

    def __init__(self,userName,chatString):

        self.userName = userName

        self.chatString = chatString

        # self.chat = input('Type in chat [q to quit]: ')

    def Process(self):

        self.Handle_New_User()

        self.Handle_Returning_User()

# ----------------- Private methods ---------------------

    def Handle_New_User(self):

        if self.userName == 'newbie':

            print('Welcome!')

    def Handle_Returning_User(self):

        if self.userName == 'veteran':

            pass
