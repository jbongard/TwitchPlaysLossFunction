from chat import CHAT

import sys

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

# ----------------------------- Main function ------------------------

userName , chatString = Get_UserName_And_ChatString()

while True:

    chat = CHAT(userName,chatString) 

    exit()
