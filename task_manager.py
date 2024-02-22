# Notes: 
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise
# the program will look in your root directory for the text files.


#=====importing libraries===========
from tabulate import tabulate
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"


# Create tasks.txt if it doesn"t exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as task_file:
        pass

with open("tasks.txt", "r") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t["username"] = task_components[0]
    curr_t["title"] = task_components[1]
    curr_t["description"] = task_components[2]
    curr_t["assigned_date"] = datetime.strptime(task_components[3],
                                                DATETIME_STRING_FORMAT)
    curr_t["due_date"] = datetime.strptime(task_components[4],
                                           DATETIME_STRING_FORMAT)
    curr_t["completed"] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====

"""
This code reads usernames and password from the user.txt file to
allow a user to login.
"""

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", "r") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(";")
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


#====New functions added====


def reg_user():
    """
    The `reg_user()` function allows a user to register a new username and
    password, and stores the information in a file called "user.txt".
    """
    
    while True:

        # Request input of a new username
        new_username = input("New Username: ")

        if new_username not in username_password.keys():

            # Request input of a new password
            new_password = input("New Password: ")

            # Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

            # Check if new password and confirmed password are the same.
            if new_password == confirm_password:
                # If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password

                with open("user.txt", "w") as user_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    user_file.write("\n".join(user_data))

                break

            # Otherwise you present a relevant message.
            else:
                print("Passwords do no match")

        else:
            print("This username already exists. Please try a new one.\n")

# ====end def====


def add_task():
    """
    The `add_task` function allows the user to input details of a task and
    adds it to a task list stored in a file.
    """

    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        exit()
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = datetime.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "assigned_date": curr_date,
        "due_date": due_date_time,
        "completed": False
    }

    # Append new task to existing task list
    task_list.append(new_task)

    # Open tasks file in write mode
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t["username"],
                t["title"],
                t["description"],
                t["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                t["due_date"].strftime(DATETIME_STRING_FORMAT),      
                "Yes" if t["completed"] else "No"
            ]                                    
            task_list_to_write.append(";".join(str_attrs))

        # Rewrite file with updated task list
        task_file.write("\n".join(task_list_to_write))

    print("Task successfully added.")

# ====end def====


def view_all():

    """
    Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """

    for t in task_list:
        disp_str = f"Task: \t\t {t["title"]}\n"
        disp_str += f"Assigned to: \t {t["username"]}\n"
        disp_str += f"Date Assigned: \t {t["assigned_date"].strftime(
            DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t["due_date"].strftime(
            DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t["description"]}\n"
        disp_str += f"Completed: \t {t["completed"]}\n"
        print(disp_str)

# ====end def====


def read_and_write_task_file(task_position, new_task):
    """
    The function reads a file called "tasks.txt", updates a specific task at
    a given position with a new task, and writes the updated tasks back to
    the file.
    
    :param task_position: The position of the task in the file that needs to
    be updated
    :param new_task: The new task that you want to write to the file
    """    

    with open("tasks.txt", "r+") as task_file:

        task_data[task_position] = new_task

        for line in task_data:
            task_file.write(f"{line}\n")

# ====end def====


def update_task(task_choice, update_location, new_value):
    """
    The function `update_task` updates a specific task in a task list with a
    new value for a specified attribute and writes the updated task to a
    file.
    
    :param task_choice: The task_choice parameter represents the index of the
    task in the task_list that you want to update
    :param update_location: The `update_location` parameter is the location
    within the task that you want to update. It could be any attribute of the
    task such as the username, title, description, assigned date, due date,
    or completion status
    :param new_value: The `new_value` parameter is the value that you want to
    update in the task. It could be a new title, description, assigned date,
    due date, or completion status
    """
    
    for task_number, t in enumerate(task_list):
        
        if task_choice == task_number:

            # Update completion status
            t[update_location] = new_value
                                            
            updated_task = f"{t["username"]};"
            updated_task += f"{t["title"]};"
            updated_task += f"{t["description"]};"
            updated_task += f"{t["assigned_date"].strftime(
                DATETIME_STRING_FORMAT)};"
            updated_task += f"{t["due_date"].strftime(
                DATETIME_STRING_FORMAT)};"
            updated_task += f"{t["completed"]}"
    
    read_and_write_task_file(task_choice, updated_task)

# ====end def====


def edit_task(task_choice):
    """
    The function `edit_task` allows the user to edit the username of the
    responsible officer or the due date of a task.
    
    :param task_choice: The parameter `task_choice` represents the index or
    identifier of the task that the user wants to edit. It is used to
    identify the specific task in the `task_list` that needs to be edited
    """    

    print("Enter -\n'u' to edit the username of the responsible officer,",
          "or\n'd' to edit the due date")
    
    edit_choice = input(": ").lower()

    # Edit username
    if edit_choice == "u":

        print("Enter the username of the new officer")
        
        new_username = input(": ")

        # Check if new username is valid
        if new_username in username_password.keys():
            
            update_task(task_choice,
                        "username", new_username)

            print("The new officer responsible for",
                  f"Task: {task_list[ task_choice]["title"]}",
                  f"is changed to {new_username}.")

            return

        # Error message for invalid username
        else:
            print("No such user. Please try again.")


    # Edit due date
    elif edit_choice == "d":

        while True:

            try:

                print("New due date of task (YYYY-MM-DD)")
                
                new_task_due_date = input(": ")
                
                new_due_date_time = datetime.strptime(new_task_due_date,
                    DATETIME_STRING_FORMAT)
                
                update_task(task_choice,
                            "due_date",
                            new_due_date_time)

                print(f"The due date of Task: {task_list[task_choice]["title"]}",
                    "is changed to",
                    f"{new_due_date_time.strftime(DATETIME_STRING_FORMAT)}.")

                break

            # Error message for invalid datetime format
            except ValueError:
                print("Invalid datetime format.",
                      "Please use the format specified.")

    # Error message for not entering "u" or "d"
    else:
        print("Invalid input. Please try again.")

# ====end def====


def mark_complete_or_edit_task(task_choice):
    """
    The function `mark_complete_or_edit_task` allows a user to mark a task as
    complete or edit a task, based on their input.
    
    :param task_choice: The parameter `task_choice` represents the user's
    choice of task to mark as complete or edit. It is an integer value that
    corresponds to the index of the task in the `task_list` array
    """

    for task_number, t in enumerate(task_list):

        # Go back to main menu (task_choice -1 so "-2")
        if task_choice == -2:
            break

        # Error message for not entering a task that belongs to others
        elif task_choice == task_number and t["username"] != curr_user:
            print("This task is not assigned to you. Please try again.")

        # If task_choice is valid and task belongs to current user
        elif task_choice == task_number and t["username"] == curr_user:

            while True:

                # Ask user to mark task complete, edit task, or
                # return to main menu; 
                # alphabetical input is kept to lower case
                print("Enter -\n 'c' to mark task as complete, or",
                        "\n'e' to edit it, or",
                        "\n'-1' to return to the main menu")
                
                action_choice = input(": ").lower()

                # Go back to main menu
                if action_choice == "-1":
                    break

                # Mark task complete
                elif action_choice == "c":

                    update_task(task_choice, "completed", "Yes")

                    print(f"Task: {task_list[task_choice]["title"]}",
                            "is marked as complete.")

                    break

                # Edit username or due date
                elif action_choice == "e":

                    # Error message for choosing to edit completed tasks
                    if t["completed"] == "Yes" or \
                        t["completed"] is True:
                        print("The task is completed and",
                                "cannot be edited.")
                        break

                    else:
                        edit_task(task_choice)
                        
                # Error message for not entering "-1", "c" or "e"
                else:
                    print("Invalid input. Please try again.")

# ====end def====


def view_mine():
    """
    The `view_mine` function reads tasks from a file and prints them to the
    console in format of Output 2 presented in the task pdf (i.e. includes
    spacing and labelling), allowing the user to mark a task as complete or
    edit it.
    """

    # Display error message if no task is assigned to current user
    user_task_count = 0
    for task_number, t in enumerate(task_list):

        # Check if user has any task; if not, show error message
        if t["username"] != curr_user:
            user_task_count += 1

            if user_task_count == len(task_list):
                print("You have not been assigned any task yet.")

        else:
            # Task number added
            disp_str = f"Task number: \t {task_number + 1}\n"
            disp_str += f"Task: \t\t {t["title"]}\n"
            disp_str += f"Assigned to: \t {t["username"]}\n"
            disp_str += f"Date Assigned: \t {t["assigned_date"].strftime(
                DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t["due_date"].strftime(
                DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t["description"]}\n"
            disp_str += f"Completed: \t {t["completed"]}\n"
            print(disp_str)

    try:

        # Ask user to mark completion of or edit a task
        # or return to main menu
        print("Enter -\nthe number of a task (e.g. '1')",
              "to mark complete or edit it, or\n'-1' to return to main menu")
                                
        task_choice = int(input(": ")) - 1

        if 0 < task_choice > len(task_list):
            print("Invalid input. Please try again.")

        else:

            mark_complete_or_edit_task(task_choice)

    # Error message for not entering an integer
    except ValueError:
        print("Invalid input. Please enter a number.")

# ====end def====


def task_overview_report():
    """
    The `task_overview_report` function generates a report on the overview of
    tasks, including the total number of tasks, completed tasks, uncompleted
    tasks, overdue tasks, and the percentage of uncompleted and overdue
    tasks.
    """

    # Read all information required from tasks.txt first

    # The total number of tasks
    num_tasks = len(task_list)


    # The total number of completed tasks
    num_completed_tasks = 0

    for t in task_list:
        if t["completed"] is True:
            num_completed_tasks += 1


    # The total number of uncompleted tasks
    num_uncompleted_tasks = 0

    for t in task_list:
        if t["completed"] is False:
            num_uncompleted_tasks += 1


    # The total number of uncompleted and overdue tasks
    curr_date = datetime.today()
    num_overdue_tasks = 0

    for t in task_list:
        if t["completed"] is False and curr_date > t["due_date"]:
            num_overdue_tasks += 1


    # The percentage of tasks that are uncompleted
    try:
        pct_uncompleted_tasks = f"{round(
            num_uncompleted_tasks / num_tasks * 100, 2)}%"

    except ZeroDivisionError:
        pct_uncompleted_tasks = "N/A - no task assigned to user"


    # The percentage of tasks that are overdue
    try:
        pct_overdue_tasks = f"{round(num_overdue_tasks / num_tasks * 100, 2)}%"


    except ZeroDivisionError:
        pct_overdue_tasks = "N/A - no task assigned to user"


    # Create task overview table with tabulate
    task_overview_table = [
        ["Total number of tasks logged:", num_tasks],
        ["Total number of completed tasks:", num_completed_tasks],
        ["Total number of uncompleted tasks:", num_uncompleted_tasks],
        ["Total number of overdue tasks:", num_overdue_tasks],
        ["Percentage of uncompleted tasks:", pct_uncompleted_tasks],
        ["Percentage of overdue tasks:", pct_overdue_tasks]
    ]

    task_overview_data = f"\nTask Overview Report\nPrint Date: {date.today()}\n"
    task_overview_data += tabulate(task_overview_table)


    # Create task overview text file and write
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(task_overview_data)

    # Print file content
    with open("task_overview.txt", "r") as task_overview_file:
        task_overview = task_overview_file.readlines()
        for line in task_overview:
            print(line, sep="\n")

# ====end def====


def user_overview_report():
    """
    The `user_overview_report` function generates a report that provides an
    overview of user statistics and task information.
    """

    # The total number of users registered
    num_users = len(username_password.keys())


    # The total number of tasks logged
    num_tasks = len(task_list)


    # General data to be printed above data for each user
    user_overview_data = f"\nUser Overview Report\nPrint Date: {date.today()}\n"
    user_overview_data += "-" * 45 + "\n"
    user_overview_data += f"The total number of users registered: {num_users}\n"
    user_overview_data += f"The total number of tasks logged: {num_tasks}\n"


    # Looping through each user
    for user in username_password.keys():

        curr_date = datetime.today()
        num_tasks_by_user = 0
        num_completed_tasks_by_user = 0
        num_uncompleted_tasks_by_user = 0
        num_overdue_tasks_by_user = 0


        # Looping through each tasks to find:
        # The total number of tasks assigned to each user
        for t in task_list:
            if user == t["username"]:
                num_tasks_by_user += 1


            # The percentage of the total number of tasks that have been
            # assigned to each user
            try:
                pct_tasks_by_user = f"{round(num_tasks_by_user / num_tasks * \
                    100, 2)}%"

            except ZeroDivisionError:
                pct_tasks_by_user = "N/A - no task assigned to user"


            # The number of completed tasks by user
            if user == t["username"] and t["completed"] is True:
                num_completed_tasks_by_user += 1


            # The percentage of tasks assigned to each user that have
            # been completed
            try:
                pct_completed_tasks_by_user = f"{round(
                    num_completed_tasks_by_user / num_tasks_by_user * 100, 2)}%"

            except ZeroDivisionError:
                pct_completed_tasks_by_user = "N/A - no task assigned to user"


            # The number of uncompleted tasks by user
            if user == t["username"] and t["completed"] is False:
                num_uncompleted_tasks_by_user += 1


            # The percentage of tasks assigned to each user that have
            # been uncompleted
            try:
                pct_uncompleted_tasks_by_user = f"{round(
                    num_uncompleted_tasks_by_user / num_tasks_by_user * 100, 2)
                    }%"

            except ZeroDivisionError:
                pct_uncompleted_tasks_by_user = "N/A - no task assigned to user"


            # The number of overdue tasks by user
            if user == t["username"] and t["completed"] is False and \
                curr_date > t["due_date"]:
                num_overdue_tasks_by_user += 1


            # The percentage of tasks assigned to each user that are overdue
            try:
                pct_overdue_tasks_by_user = f"{round(
                    num_overdue_tasks_by_user / num_tasks_by_user * 100, 2)}%"

            except ZeroDivisionError:
                pct_overdue_tasks_by_user = "N/A - no task assigned to user"


        # Create user overview table with tabulate
        user_overview_table_by_user = [
            ["Username:", user],
            ["Total number of tasks assigned to user:",
            num_tasks_by_user],
            ["Percentage of total number of tasks that have been assigned to user:",
            pct_tasks_by_user],
            ["Percentage of tasks assigned to user that have been completed:",
            pct_completed_tasks_by_user],
            ["Percentage of tasks assigned to user that have been uncompleted:",
            pct_uncompleted_tasks_by_user],
            ["Percentage of tasks assigned to user that are overdue:",
            pct_overdue_tasks_by_user]
        ]


        # Collect all user overview data
        user_overview_data += f"{tabulate(user_overview_table_by_user)}\n"


    # Create task overview text file and write
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(user_overview_data)


    # Print file content
    with open("user_overview.txt", "r") as user_overview_file:
        user_overview = user_overview_file.readlines()
        for line in user_overview:
            print(line, sep="\n")


# ====end def====


def gen_reports():
    """
    If the user is an admin, they can generate two reports: 
    task overview and user overview.
    """

    # Ask user to choose which report; input is kept to lower case
    report = input("Enter -\n'u' to generate the user overview report " +
                    "or\n't' to generate the task overview report\n: "
                    ).lower()

    if report == 'u':
        user_overview_report()

        # Allow user to return to main menu
        os.system("pause")

    elif report == 't':
        task_overview_report()

        # Allow user to return to main menu
        os.system("pause")

    else:
        print("You have made a wrong choice, Please Try again")

# end def


def disp_statistics():
    """
    The function `disp_statistics` displays user statistics (number of users
    and their usernames and passwords) and task statistics (number of tasks
    and all task details) and allows the user to return to the main menu.
    """
    
    # Print user statistics:
    # total number of users, and usernames and passwords
    num_users = len(username_password.keys())
    print("-" * 60 + "\nUSER STATISTICS")
    print(f"Number of users: {num_users}\n")
    print("Usernames & passwords -\n")

    for user in user_data:
        username, password = user.split(";")
        username_password[username] = password
        print(f"\nUsername: {username}")
        print(f"Password: {password}\n" + "*" * 40)


    # Print tasks statistics:
    # total number of tasks, and all task details
    num_tasks = len(task_list)
    print("-" * 60 + "\nTASKS STATISTICS")
    print(f"Number of tasks logged: {num_tasks}\n")
    print("All task details -\n")
    view_all()
    print("-" * 60)


    # Allow user to return to main menu
    os.system("pause")

# end def


#====Menu====
# The code below is creating a menu-driven program that allows users to
# perform various tasks. It uses a while loop to continuously display the
# menu and prompt the user for their choice.

while True:
    
    print()
    menu = input("""Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: """).lower()

    if menu == "r":
        # Call function to register new user
        reg_user()

    elif menu == "a":
        # Call function to add a task
        add_task()

    elif menu == "va":
        # Call function to view all tasks
        view_all()

    elif menu == "vm":
        # Call function to view the user"s task
        view_mine()

    elif menu == "gr" and curr_user == "admin":
        # Call function to generate reports
        gen_reports()

    elif menu == "gr" and curr_user != "admin":
        # Error message for those without access right
        print("Sorry, you do not have access right for this.")

    elif menu == "ds" and curr_user == "admin":
        # Call function to display statistics
        disp_statistics()

    elif menu == "ds" and curr_user != "admin":
        # Error message for those without access right
        print("Sorry, you do not have access right for this.")

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
