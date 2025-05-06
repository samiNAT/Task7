import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# File to save tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Loads the list of tasks from the tasks.json file.
    Returns a list of tasks or an empty list if the file doesn't exist.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """
    Saves the list of tasks to the tasks.json file in JSON format.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, task_name):
    """
    Adds a new task to the list and saves the updated list to the file.
    """
    tasks.append({"name": task_name, "done": False})
    logging.info(f"Task '{task_name}' added.")
    save_tasks(tasks)

def mark_task_done(tasks, task_index):
    """
    Marks a task as done based on its index in the list.
    Logs an error if the index is invalid.
    """
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        logging.info(f"Task '{tasks[task_index]['name']}' marked as done.")
        save_tasks(tasks)
    else:
        logging.error("Invalid task index.")

def list_tasks(tasks):
    """
    Logs all tasks in the list along with their status.
    If the list is empty, logs a message indicating no tasks are found.
    """
    if not tasks:
        logging.info("No tasks found!")
        return
    logging.info("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        logging.info(f"{i}. {task['name']} [{status}]")

def display_menu():
    """
    Displays the main menu options for the To-Do app.
    """
    print("\nCommand Line To-Do App")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. List All Tasks")
    print("4. Exit")

def handle_choice(choice, tasks):
    """
    Handles the user's menu choice and performs the corresponding action.
    """
    if choice == "1":
        task_name = input("Enter the task name: ").strip()
        add_task(tasks, task_name)
    elif choice == "2":
        list_tasks(tasks)
        try:
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            mark_task_done(tasks, task_index)
        except ValueError:
            logging.error("Please enter a valid number.")
    elif choice == "3":
        list_tasks(tasks)
    elif choice == "4":
        logging.info("Exiting To-Do App. Goodbye!")
        return False
    else:
        logging.error("Invalid choice. Please try again.")
    return True

def main():
    """
    Main function that provides a command-line interface for the To-Do app.
    """
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if not handle_choice(choice, tasks):
            break

if __name__ == "__main__":
    main()