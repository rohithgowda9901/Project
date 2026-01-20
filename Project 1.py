# At the start of the day you have a checklist The tasks which you were able to finish, should get added 
# to completed_tasks The tasks which you were not able to finish, should get added to incomplete_tasks 
# This project is about organizing your daily tasks into two categories: completed tasks and incomplete 
# tasks. Here’s how it works: 1. At the start of the day, you create a checklist of tasks you want to 
# accomplish. 2. At the end of the day, you review which tasks you could finish and which you couldn’t. 
# – If a task is finished, you move it to the completed tasks list. – If a task is not finished, you 
# move it to the incomplete tasks list. This way, by the end of each day, you’ll have a clear overview 
# of what you completed and what still needs attention.

# Define the lists of completed and incomplete tasks
completed_tasks = ['Check emails', 'Attend meeting']
incomplete_tasks = ['Write report', 'Update website']

# Get input from the user and remove any leading/trailing whitespace
task_to_check = input("Enter the task you want to check: ").strip().capitalize()

# Check which list the task belongs to and print the status
if task_to_check in completed_tasks:
    print(f"'{task_to_check}' is a COMPLETED task.")
elif task_to_check in incomplete_tasks:
    print(f"'{task_to_check}' is an INCOMPLETE task.")
else:
    print(f"The task '{task_to_check}' was not found in the checklists.")