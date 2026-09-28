"""
Password Generator
A beginner-friendly password generator that creates secure, random passwords
using Python's built-in 'random' and 'string' modules.
"""

import random
import string


def generate_password(length):
    """
    Generate a random password of a given length.
    Ensures a mixture of uppercase, lowercase, numbers, and symbols.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Full pool of possible characters
    all_characters = lowercase + uppercase + digits + symbols

    # If length is at least 4, guarantee at least one from each character group
    if length >= 4:
        password_chars = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols),
        ]
        # Fill remaining length with random choices from the complete pool
        for _ in range(length - 4):
            password_chars.append(random.choice(all_characters))

        # Shuffle the list so the guaranteed types are not always at the start
        random.shuffle(password_chars)
        return "".join(password_chars)

    # For shorter lengths (e.g., 1-3), pick purely from the full pool
    password_chars = [random.choice(all_characters) for _ in range(length)]
    return "".join(password_chars)


def get_password_length():
    """
    Prompt user for password length and validate that it is a positive integer.
    """
    while True:
        user_input = input("Enter desired password length (minimum 4, recommended 12+): ").strip()
        try:
            length = int(user_input)
            if length < 4:
                print("For basic security, password length must be at least 4.")
            elif length > 128:
                print("Length is too high! Please choose a length under 128.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 12).")


def main():
    """Main CLI program loop."""
    print("=" * 45)
    print("       RANDOM PASSWORD GENERATOR CLI         ")
    print("=" * 45)
    print("Creates strong passwords using letters,")
    print("digits, and special symbols.\n")

    while True:
        length = get_password_length()
        password = generate_password(length)

        print("\n" + "-" * 45)
        print(f"Generated Password ({length} chars):")
        print(f"  {password}")
        print("-" * 45)

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nStay safe online! Goodbye.")
            break
        print()


if __name__ == "__main__":
    main()
