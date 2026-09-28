# Python Month 1: Fundamentals Portfolio (`python-month-1`)

A collection of 5 beginner-friendly Python command-line projects built to practice and demonstrate core Python fundamentals. Each project avoids external libraries, complex frameworks, and enterprise bloat, prioritizing readable, interview-ready code that can be explained line-by-line.

---

## Project Structure

```text
python-month-1/
├── calculator/
│   ├── calculator.py
│   └── README.md
├── file-organizer/
│   ├── organizer.py
│   └── README.md
├── todo-cli/
│   ├── todo.py
│   └── README.md
├── password-generator/
│   ├── password_generator.py
│   └── README.md
├── data-analyzer/
│   ├── analyzer.py
│   └── README.md
├── .gitignore
└── README.md
```

---

## Projects Overview

| # | Project | Description | Core Topics Covered |
|---|---------|-------------|---------------------|
| 1 | **[Calculator](calculator/)** | Menu-driven arithmetic CLI with zero-division handling and user input validation. | Functions, arithmetic operators, `try...except`, `while` loops. |
| 2 | **[File Organizer](file-organizer/)** | File management script that sorts loose files into category folders based on file extensions. | `os`, `shutil`, dictionaries, file paths, defensive checks. |
| 3 | **[To-Do CLI](todo-cli/)** | Terminal task manager supporting adding, viewing, marking, and deleting tasks. | Lists, dictionaries, `enumerate()`, `.append()`, `.pop()`. |
| 4 | **[Password Generator](password-generator/)** | Configurable generator creating randomized passwords with guaranteed character diversity. | `random`, `string`, list shuffling, input constraints. |
| 5 | **[Data Analyzer](data-analyzer/)** | CLI statistics calculator computing count, sum, mean, min, max, and median. | Statistics logic, list slicing, sorting, accumulator loops. |

---

## Skills & Fundamentals Demonstrated

- **Core Data Types & Variables:** `int`, `float`, `str`, `bool`, type conversion, and immutability.
- **Data Structures:** 
  - `list`: appending, popping, indexing, slicing, and iterating.
  - `dict`: key-value mappings for file categories and task representations.
  - `set`: fast membership testing.
- **Control Flow:** `if / elif / else` branching, `for` loops, `while` loops, `break`, and `continue`.
- **Functions & Modularity:** Writing clear functions with descriptive parameters, return values, and docstrings.
- **Error & Exception Handling:** Handling `ValueError` during input casting, `ZeroDivisionError` during calculations, and general exceptions during file operations.
- **Standard Library Modules:** `os`, `shutil`, `random`, `string`.
- **Clean CLI Interactions:** Input sanitization (`.strip()`), menu loops, and clean output formatting using Python f-strings.

---

## How to Run the Projects

### Prerequisites
- Python 3.8 or higher installed on your system.
- No third-party packages or virtual environment activation needed; all scripts use Python's built-in standard library.

### Running a Project
Open a terminal in the root directory and run any of the scripts:

```bash
# 1. Calculator
python calculator/calculator.py

# 2. File Organizer
python file-organizer/organizer.py

# 3. To-Do CLI
python todo-cli/todo.py

# 4. Password Generator
python password-generator/password_generator.py

# 5. Data Analyzer
python data-analyzer/analyzer.py
```

---

## What I Learned

Throughout building these 5 projects during Month 1:

1. **Thinking in Functions:** Breaking down a problem into small, single-purpose functions makes debugging and testing straightforward.
2. **Defensive Programming:** Real users rarely enter what you expect. Handling invalid inputs with `try...except` and input-checking loops is essential for crash-free applications.
3. **Power of the Python Standard Library:** Python comes with "batteries included". Modules like `os`, `shutil`, `random`, and `string` provide substantial functionality without needing external dependencies.
4. **Data Structure Selection:** Choosing between a list, a dictionary, or a set depends on how data is accessed and modified (e.g., ordered items vs. category mappings).
5. **Code Explainability:** Writing clear variable names and concise logic makes it easy to walk through any line of code during technical discussions and interviews.
