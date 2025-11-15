from task_track import greet
from task_track.functionality import function_map_dict
from task_track.functionality import exit_app
import os


while True:
    choice = greet()
    function_map_dict[choice]()
    ask_user=input("Type yes to continue or type 'exit' to quit: ")
    if ask_user.lower()=='yes':
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
    elif ask_user.lower()=='exit':
        exit_app()
    else:
        print("Invalid input. Exiting the program.")
        exit_app()