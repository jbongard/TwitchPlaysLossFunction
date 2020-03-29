from chat import CHAT

chat = CHAT()

while not chat.Quit_Desired():

    if chat.Valid_Fitness_Variable():

        chat.Print_Fitness_Variable_Entered_Successfully()

    else:

        chat.Print_Fitness_Variable_Entered_Unsuccessfully()

    chat = CHAT()
