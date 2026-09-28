"""
Simple Calculator
A clean, beginner-friendly command-line calculator demonstrating
Python functions, user input, conditional logic, and error handling.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Return the division of a by b.
    Raises ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """
    Safely get a floating-point number from user input.
    Repeats until the user enters a valid number.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 5 or 3.14).")


def display_menu():
    """Print the calculator menu options."""
    print("\n" + "=" * 30)
    print("      SIMPLE CALCULATOR       ")
    print("=" * 30)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("=" * 30)


def main():
    """Main program loop."""
    print("Welcome to the Simple Calculator!")

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the Simple Calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Please choose a number between 1 and 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == "4":
            try:
                result = divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
            except ZeroDivisionError as error:
                print(f"\nError: {error}")


if __name__ == "__main__":
    main()
