from task_track.dict_main import add_to_dict, get_from_dict, remove_from_dict, clear_dict, dict_size, dict_keys, dict_values, dict_items, update_dict, dict_exists, dict_is_empty, dict_get_all
import sys
task_id = 0

task = ""
def view_tasks():
    print("Here are your current tasks:")
    tasks = dict_get_all()
    if not tasks:
        print("No tasks available.")
        pass
    print(tasks)
    return

def add_task():
    global task_id
    print("Functionality to add a new task.")
    task = input("Enter the task description: ")
    task_id += 1
    add_to_dict(task_id,task)
    print(f"Task added with ID: {task_id}")
    

def delete_task():
    print("Functionality to delete a task.")
    task_id = int(input("Enter the task ID to delete: "))
    if dict_exists(task_id):
        remove_from_dict(task_id)
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"No task found with ID {task_id}.")
        return

def exit_app():
    print("Exiting the program. Goodbye!")
    exit()

function_map_dict = {
    "1": view_tasks,
    "2": add_task,
    "3": delete_task,
    "4": exit_app
}
    
