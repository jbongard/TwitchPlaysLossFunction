class CHAT:

    def __init__(self):

        self.chat = input('Type in chat [q to quit]: ')

    def Print_Fitness_Variable_Entered_Successfully(self):

        print('success!')

    def Print_Fitness_Variable_Entered_Unsuccessfully(self):

        print('failure!')

    def Quit_Desired(self):

        return self.chat == 'q'

    def Valid_Fitness_Variable(self):

        return len(self.chat) == 1 and self.chat >= 'a' and self.chat <= 'z'
