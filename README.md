
# Python Task Manager

This programme is a menu-driven task management system that allows users to register, add tasks, view tasks, generate reports, display statistics, and perform various task-related actions. This programme can be used by families, a group of friends and even small companies to keep track of the tasks they have and call for practical statistics and reports.
## Installation

You can download my project from here:  
<https://github.com/kristy-lam/finalCapstone/blob/master/task_manager.py>  
and click the "copy" or "download" button
## Usage/Examples

### Using the code for the first time
Login as administrator with the details below:  
Username: **admin**  
Password: **password**  

![Login](/login.png)  

### Function 1: Registering a user
After logging in, you can create a new user if necessary.  
1. Type in "r" to register a user.
2. Type in a new user name.
3. Type in a password.
4. Type in the password again to confirm.
5. If the two passwords match, the new user will be created and the success message will be shown.

![User registration successful](/register-success.png)

If a user already exists, you will see an error message.  

![User registration error - user already exists](/register-error1.png)

If the two passwords do not match, you won't be able to proceed further until they match.

![User registration error - passwords not matching](/register-error2.png)

### Function 2: Adding a task

You can add a task to any user already registered.
1. Type in "a" to register a user.
2. Type in the username of the user you want assign.
3. Type in the title of the task and description.
4. Type in the due date according to the format stated: YYYY-MM-DD.
5. If all information is inputted correctly, a success message will be shown.

![Adding a task](/add-success.png)

If you type in a user which has not been registered, you will not be able to proceed further.

![Adding a task - user does not exist](/add-error1.png)

If you do not type in the due date in the correct format, you will be asked to type it in in the correct format again.

![Adding a task - wrong due date format](/add-error2.png)

### Function 3: View all tasks

You can view all tasks by typing in "va".

![View all tasks](/viewall.png)

### Function 4: View my tasks

You can view the user's tasks by typing in "vm". After showing the task details, you will have the option to mark a task as complete or edit it.

![View my tasks](/viewmy.png)

You can type in the task number, then choose whether to mark it as completed by typing "c", or edit the task's responsible user by typing "u" or its due date by typing "d".   

Mark as complete:
![View my tasks - mark as complete](/viewmy-complete.png)

Edit:
![View my tasks - edit](/viewmy-edit.png)

Once a task is marked as complete, you will not be able to edit it again.    

![View my tasks - edit completed task](/viewmy-edit-error1.png)

Again, an error message will be shown if you type in a user which does not exist, or type in the due date in the wrong format.

### Function 5: Generate reports

As the administrator, you can generate reports by typing "gr". Then, you can choose between a User Overview Report by typing "u" and a Task Overview Report by typing "t".

An example of the User Overview Report is shown below. A separate file named "user-overview.txt" will be created as well.

![Generate reports - User Overview Report part 1](/report-user1.png)

![Generate reports - User Overview Report part 2](/report-user2.png)

An example of the Task Overview Report is shown below. A separate file named "task-overview.txt" will be created as well.

![Generate reports - Task Overview Report](/report-task.png)

If you are not logged in as the administrator, you will not be able to view the reports and an error message will be shown.

![Generate reports - not admin error](/report-error.png)

### Function 6: Display statistics

As the administrator, you can generate statistics by typing "ds". All available statistics on both users and tasks will be displayed as shown below.

![Display statistics - users part](/stat-users.png)
![Display statistics - tasks part](/stat-tasks.png)

If you are not logged in as the administrator, you will not be able to view the statistics and an error message will be shown.

![Display statistics - not admin error](/stat-error.png)

## Authors

- [@kristy-lam](https://www.github.com/kristy-lam)
- Marked by HyperionDev tutors [@skills-cogrammar](https://github.com/skills-cogrammar)
