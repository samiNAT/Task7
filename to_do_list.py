import os
import json

# File to save tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    """
    Loads the list of tasks from the tasks.json file.
    - If the file exists, it reads the JSON data and returns it as a Python list.
    - If the file does not exist, it returns an empty list.
    """
    if os.path.exists(TASKS_FILE):  # Check if the file exists
        with open(TASKS_FILE, "r") as f:  # Open the file in read mode
            return json.load(f)  # Load and return the JSON data as a Python list
    return []  # Return an empty list if the file doesn't exist

# Save tasks to file
def save_tasks(tasks):
    """
    Saves the list of tasks to the tasks.json file.
    - The tasks are written in JSON format with indentation for readability.
    """
    with open(TASKS_FILE, "w") as f:  # Open the file in write mode
        json.dump(tasks, f, indent=4)  # Write the tasks list to the file in JSON format

# Add a new task
def add_task(tasks, task_name):
    """
    Adds a new task to the list.
    - Each task is represented as a dictionary with 'name' and 'done' keys.
    - The 'done' key is initially set to False.
    - After adding the task, the updated list is saved to the file.
    """
    tasks.append({"name": task_name, "done": False})  # Add the new task to the list
    print(f"Task '{task_name}' added.")  # Inform the user
    save_tasks(tasks)  # Save the updated tasks list to the file

# Mark a task as done
def mark_task_done(tasks, task_index):
    """
    Marks a task as done based on its index in the list.
    - If the index is valid, the 'done' key of the task is set to True.
    - The updated list is then saved to the file.
    - If the index is invalid, an error message is displayed.
    """
    if 0 <= task_index < len(tasks):  # Check if the index is valid
        tasks[task_index]["done"] = True  # Mark the task as done
        print(f"Task '{tasks[task_index]['name']}' marked as done.")  # Inform the user
        save_tasks(tasks)  # Save the updated tasks list to the file
    else:
        print("Invalid task index.")  # Display an error message if the index is invalid

# List all tasks
def list_tasks(tasks):
    """
    Displays all tasks in the list along with their status.
    - If the list is empty, it informs the user that no tasks are found.
    - Otherwise, it prints each task with its index and status (Done/Not Done).
    """
    if not tasks:  # Check if the tasks list is empty
        print("No tasks found!")  # Inform the user
        return
    print("\nTo-Do List:")  # Header for the task list
    for i, task in enumerate(tasks):  # Loop through the tasks with their indices
        status = "Done" if task["done"] else "Not Done"  # Determine the task's status
        print(f"{i + 1}. {task['name']} [{status}]")  # Print the task with its index and status

# Main command-line interface
def main():
    """
    The main function that provides a command-line interface for the To-Do app.
    - It loads tasks from the file and enters a loop to accept user commands.
    - The user can add tasks, mark tasks as done, list tasks, or exit the app.
    """
    tasks = load_tasks()  # Load tasks from the file
    while True:  # Infinite loop to keep the app running until the user exits
        print("\nCommand Line To-Do App")  # App header
        print("1. Add Task")  # Option 1: Add a new task
        print("2. Mark Task as Done")  # Option 2: Mark a task as done
        print("3. List All Tasks")  # Option 3: List all tasks
        print("4. Exit")  # Option 4: Exit the app
        choice = input("Enter your choice (1-4): ").strip()  # Get the user's choice

        if choice == "1":  # Add a new task
            task_name = input("Enter the task name: ").strip()  # Get the task name from the user
            add_task(tasks, task_name)  # Call the add_task function
        elif choice == "2":  # Mark a task as done
            list_tasks(tasks)  # Display the list of tasks
            try:
                task_index = int(input("Enter the task number to mark as done: ")) - 1  # Get the task index
                mark_task_done(tasks, task_index)  # Call the mark_task_done function
            except ValueError:  # Handle invalid input (non-integer)
                print("Please enter a valid number.")
        elif choice == "3":  # List all tasks
            list_tasks(tasks)  # Call the list_tasks function
        elif choice == "4":  # Exit the app
            print("Exiting To-Do App. Goodbye!")  # Inform the user
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choices

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the app