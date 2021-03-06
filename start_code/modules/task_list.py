
# Functions to complete:


def get_tasks_by_status(list, status):
    ### is there a verison of this where refatoring the arg status is not necessary??
    if status == "completed":
        status = True
    elif status == "uncompleted":
        status = False
    tasks_by_status = []
    for task in list:
        if task["completed"] == status:
            tasks_by_status.append(task["description"])
        else:
            pass
    return tasks_by_status
    


## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks
    # uncompleted_tasks = get_tasks_by_status(list, "uncompleted")
    # return uncompleted_tasks


## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks
    # completed_tasks = get_tasks_by_status(list, "completed")
    # return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    tasks_taking_at_least = []
    for task in list:
        if task["time_taken"] >= time:
            tasks_taking_at_least.append(task)
    return tasks_taking_at_least

# print(get_tasks_taking_at_least(tasks, 6))

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

# print(get_task_with_description(tasks, "walk"))

# Extention (Function): 

## Get a list of tasks by status
# def get_tasks_by_status(list, status):
#     if status == "completed":
#         status = True
#     elif status == "uncompleted":
#         status = False
#     tasks_by_status = []
#     for task in list:
#         if task["completed"] == status:
#             tasks_by_status.append(task["description"])
#         else:
#             pass
#     return tasks_by_status

# print(get_tasks_by_status(tasks, "completed"))
# print(get_tasks_by_status(tasks, "uncompleted"))

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)



