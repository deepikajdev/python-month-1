# Simple Calculator CLI

A beginner-friendly command-line calculator that performs fundamental arithmetic operations with clean user input validation and error handling.

## Features

- **Basic Operations:** Addition, subtraction, multiplication, and division.
- **Robust Division by Zero Handling:** Catches zero division safely and alerts the user without crashing.
- **Input Validation:** Safely handles non-numeric inputs using `try...except`.
- **Interactive Menu Loop:** Keeps running until the user explicitly chooses to exit.

## Python Concepts Learned

- **Functions:** Defining modular, single-responsibility functions (`add`, `subtract`, `multiply`, `divide`).
- **User Input & Type Casting:** Reading strings with `input()` and converting to numeric `float` types.
- **Control Flow:** Using `while` loops for the application lifecycle and `if / elif / else` for menu routing.
- **Exception Handling:** Managing `ValueError` during input casting and custom handling of `ZeroDivisionError`.
- **String Formatting:** Using Python f-strings for clean output presentation.
- **Python Entry Point:** Using the standard `if __name__ == "__main__":` idiom.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `calculator` folder:
   ```bash
   cd calculator
   ```
3. Run the script:
   ```bash
   python calculator.py
   ```

## Example Usage

```text
==============================
      SIMPLE CALCULATOR       
==============================
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
==============================
Choose an option (1-5): 4
Enter the first number: 25
Enter the second number: 0

Error: Cannot divide by zero.
```

## Possible Future Improvements

- Add support for exponentiation (`**`) and modulus (`%`).
- Maintain a session calculation history list.
- Allow entering full expressions directly (e.g., `12 + 4`).
