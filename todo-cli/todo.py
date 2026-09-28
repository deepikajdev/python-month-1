"""
To-Do List CLI
A beginner-friendly task manager demonstrating Python lists, dictionaries,
functions, loops, and user input validation.
"""


def display_menu():
    """Print the available menu options."""
    print("\n" + "=" * 30)
    print("         TO-DO LIST CLI        ")
    print("=" * 30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 30)


def view_tasks(tasks):
    """Display all tasks with their completion status and index numbers."""
    print("\n--- YOUR TASKS ---")
    if not tasks:
        print("Your to-do list is empty! Add a task to get started.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")


def add_task(tasks):
    """Prompt the user for a new task title and append it to the list."""
    task_title = input("\nEnter task description: ").strip()
    if not task_title:
        print("Task description cannot be empty!")
        return

    new_task = {
        "title": task_title,
        "completed": False
    }
    tasks.append(new_task)
    print(f"Added task: \"{task_title}\"")


def get_task_index(tasks, action_name):
    """
    Helper function to prompt and validate a task index from user input.
    Returns 0-based index if valid, or None if invalid.
    """
    if not tasks:
        print(f"No tasks available to {action_name}.")
        return None

    view_tasks(tasks)
    user_input = input(f"\nEnter the number of the task to {action_name}: ").strip()

    try:
        task_num = int(user_input)
        if 1 <= task_num <= len(tasks):
            return task_num - 1  # Convert to 0-based index
        else:
            print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
            return None
    except ValueError:
        print("Please enter a valid whole number.")
        return None


def mark_completed(tasks):
    """Mark a selected task as completed."""
    index = get_task_index(tasks, "mark as completed")
    if index is not None:
        if tasks[index]["completed"]:
            print(f"Task #{index + 1} is already completed!")
        else:
            tasks[index]["completed"] = True
            print(f"Task #{index + 1} (\"{tasks[index]['title']}\") marked as completed!")


def delete_task(tasks):
    """Remove a selected task from the list."""
    index = get_task_index(tasks, "delete")
    if index is not None:
        removed_task = tasks.pop(index)
        print(f"Deleted task: \"{removed_task['title']}\"")


def main():
    """Main application loop."""
    # List to hold all tasks in memory
    tasks = []

    print("Welcome to your simple CLI To-Do List manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nThank you for using To-Do List CLI. Stay productive!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()
