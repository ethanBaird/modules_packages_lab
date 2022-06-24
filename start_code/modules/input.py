
def get_option_choice():
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    return option

def get_task_description():
    task_description = input("Enter task description to search for: ")
    return task_description

def get_task_duration():
    task_duration = int(input("Enter task duration: "))
    return task_duration