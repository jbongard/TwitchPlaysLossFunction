from chat import CHAT

while True:

    chat = CHAT() 

    chat.Process_Chat()

    if chat.Quit_Desired():

        break
