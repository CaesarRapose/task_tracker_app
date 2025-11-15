from .functionality import view_tasks, add_task, delete_task, exit_app

choice = ""
# greet.py
from .functionality import view_tasks, add_task, delete_task, exit_app

def greet():
    """
    Prompt until user enters a valid choice, then return it.
    """
    print("Hello and welcome to tracking your tasks!\n")
    while True:
        choice = input(
            "Main Menu:\n"
            "1. View Tasks\n"
            "2. Add Task\n"
            "3. Delete Task\n"
            "4. Exit\n"
            "Please enter your choice (1-4): "
        ).strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        else:
            print("Invalid choice. Please select a valid option from the menu.")

    

# remain in greet.py (or move to another module if you prefer)
def function_map_dict(ch):
    """
    Accept the choice string `ch` and call the mapped function.
    """
    print(ch)
    c = {
        "1": view_tasks,
        "2": add_task,
        "3": delete_task,
        "4": exit_app
    }

    # Check membership against keys and call the function
    if ch in c:
        c[ch]()   # call the mapped function
    else:
        print("Invalid choice passed to function_map_dict:", ch)
