# To-Do CLI

A lightweight, beginner-friendly command-line task management application for tracking daily tasks and productivity directly in your terminal.

## Features

- **View Tasks:** Lists all current tasks with intuitive visual status markers (`[ ]` for pending, `[X]` for completed).
- **Add Task:** Prompts for and appends new task items to the list.
- **Mark as Completed:** Toggles a task's status to finished without removing it from sight.
- **Delete Task:** Removes a task item cleanly by its list number.
- **Input Validation:** Safely checks list bounds and handles non-integer inputs without crashing.

## Python Concepts Learned

- **Lists (`list`):** Storing ordered collections of items and modifying them using `.append()` and `.pop()`.
- **Dictionaries (`dict`):** Representing task entities as key-value pairs (`title` and `completed` boolean flag).
- **Enumeration (`enumerate()`):** Generating human-friendly 1-based indices alongside list elements.
- **Functions & Parameters:** Passing lists into functions as mutable references and modularizing repetitive validation logic.
- **Loops & Control Flow:** Maintaining the interactive CLI using a `while` loop with `if / elif / else` branching.
- **Input Parsing & Error Handling:** Handling index boundary errors and catching `ValueError` during integer conversions.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `todo-cli` folder:
   ```bash
   cd todo-cli
   ```
3. Run the script:
   ```bash
   python todo.py
   ```

## Example Usage

```text
==============================
         TO-DO LIST CLI        
==============================
1. View Tasks
2. Add Task
3. Mark Task as Completed
4. Delete Task
5. Exit
==============================
Enter your choice (1-5): 1

--- YOUR TASKS ---
1. [ ] Read chapter 3 of Python book
2. [X] Practice basic arithmetic in CLI
```

## Possible Future Improvements

- Save and load tasks to a local text file or JSON file to persist data across sessions.
- Add task priorities (e.g., High, Medium, Low).
- Add due dates and a filter to show only pending tasks.
