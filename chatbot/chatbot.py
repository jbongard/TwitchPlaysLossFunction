import sys
sys.path.insert(0, '..')

from chat              import CHAT
from database.database import DATABASE

def Get_UserName_And_ChatString():

    program_name = sys.argv[0]

    arguments = sys.argv[1:]

    numberOfArguments = len(arguments)

    if numberOfArguments != 2:

        print('Supply a user name and piece of chat (e.g. josh hello) as two command line arguments.')
        exit()

    else:
        userName   = arguments[0]
        chatString = arguments[1]
 
        return userName , chatString

def Quit_If_Requested(chatString):

    if chatString == 'q':

        exit()

# ----------------------------- Main function ------------------------

db = DATABASE()

userName , chatString = Get_UserName_And_ChatString()

while True:

    Quit_If_Requested(chatString)

    chat = CHAT(db,userName,chatString) 

    chat.Process()

    chatString = input( userName + ': ' )
