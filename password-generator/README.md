# Password Generator CLI

A customizable, beginner-friendly command-line tool that generates secure, randomized passwords combining uppercase letters, lowercase letters, numbers, and symbols.

## Features

- **Standard Library Only:** Zero external dependencies; built using Python's native modules.
- **Balanced Complexity:** Automatically ensures passwords include at least one lowercase letter, one uppercase letter, one digit, and one symbol.
- **Customizable Length:** Prompts the user for length with sensible limits and error validation.
- **Shuffled Output:** Uses in-place shuffling to prevent predictable character positioning.
- **Continuous Generation:** Generates multiple passwords in one session until the user chooses to exit.

## Python Concepts Learned

- **Built-in `string` Module:** Using character constants such as `string.ascii_lowercase`, `string.ascii_uppercase`, and `string.digits`.
- **Randomization (`random` module):** Utilizing `random.choice()` for element selection and `random.shuffle()` for in-place list reordering.
- **String Manipulation:** Combining character collections with string concatenation and converting character lists into strings using `''.join()`.
- **List Operations:** Initializing lists, using `.append()`, and list comprehensions.
- **Looping & Re-prompting:** Using `while True` input validation loops and processing user decisions (`y/n`).
- **Input Validation:** Catching `ValueError` when parsing string inputs into integers.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the `password-generator` folder:
   ```bash
   cd password-generator
   ```
3. Run the script:
   ```bash
   python password_generator.py
   ```

## Example Usage

```text
=============================================
       RANDOM PASSWORD GENERATOR CLI         
=============================================
Creates strong passwords using letters,
digits, and special symbols.

Enter desired password length (minimum 4, recommended 12+): 14

---------------------------------------------
Generated Password (14 chars):
  k9#Wp2$mQ8!zX@
---------------------------------------------

Generate another password? (y/n): n

Stay safe online! Goodbye.
```

## Possible Future Improvements

- Add option toggles so users can choose whether to exclude symbols or ambiguous characters (e.g., `l`, `1`, `O`, `0`).
- Copy the generated password automatically to the operating system clipboard.
- Include a password strength meter (e.g., Weak, Moderate, Strong).
