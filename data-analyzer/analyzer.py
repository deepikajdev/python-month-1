"""
Data Analyzer CLI
A beginner-friendly data analysis script that takes numerical input from a user,
computes essential descriptive statistics (count, sum, mean, min, max, median),
and prints a formatted summary.
"""


def calculate_count(numbers):
    """Return the total number of elements in the list."""
    return len(numbers)


def calculate_sum(numbers):
    """Return the sum of all elements in the list."""
    total = 0.0
    for num in numbers:
        total += num
    return total


def calculate_mean(numbers):
    """Return the arithmetic average (mean) of the numbers."""
    if not numbers:
        return 0.0
    return calculate_sum(numbers) / calculate_count(numbers)


def find_minimum(numbers):
    """Find and return the smallest number in the list."""
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val


def find_maximum(numbers):
    """Find and return the largest number in the list."""
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val


def calculate_median(numbers):
    """
    Calculate the median (middle value) of a list of numbers.
    If the count is odd, return the exact middle value.
    If the count is even, return the average of the two middle values.
    """
    sorted_nums = sorted(numbers)
    count = len(sorted_nums)
    mid = count // 2

    if count % 2 != 0:
        # Odd number of items: pick the middle one
        return sorted_nums[mid]
    else:
        # Even number of items: average of the two central numbers
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def parse_numbers(input_string):
    """
    Parse a string of space- or comma-separated values into a list of floats.
    Raises ValueError if any item cannot be parsed.
    """
    # Replace commas with spaces so user can enter either format
    cleaned = input_string.replace(",", " ")
    tokens = cleaned.split()

    if not tokens:
        raise ValueError("No numbers were entered.")

    numbers = []
    for token in tokens:
        numbers.append(float(token))
    return numbers


def prompt_user_for_numbers():
    """
    Keep prompting user until they provide a valid list of at least one number.
    """
    while True:
        raw_input = input("\nEnter numbers separated by spaces or commas:\n> ").strip()
        try:
            numbers = parse_numbers(raw_input)
            return numbers
        except ValueError as err:
            print(f"Invalid input: {err}. Please enter only numeric values.")


def display_analysis(numbers):
    """Display statistical analysis report."""
    count = calculate_count(numbers)
    total_sum = calculate_sum(numbers)
    mean = calculate_mean(numbers)
    minimum = find_minimum(numbers)
    maximum = find_maximum(numbers)
    median = calculate_median(numbers)

    print("\n" + "=" * 35)
    print("       DATA ANALYSIS REPORT        ")
    print("=" * 35)
    print(f"  Raw Dataset   : {numbers}")
    print(f"  Count         : {count}")
    print(f"  Sum           : {total_sum:.2f}")
    print(f"  Mean (Average): {mean:.2f}")
    print(f"  Minimum       : {minimum:.2f}")
    print(f"  Maximum       : {maximum:.2f}")
    print(f"  Median        : {median:.2f}")
    print("=" * 35)


def main():
    """Main CLI program loop."""
    print("=" * 45)
    print("            DATA ANALYZER CLI                ")
    print("=" * 45)
    print("Calculate count, sum, mean, min, max, and median")
    print("from your numerical datasets.\n")

    while True:
        numbers = prompt_user_for_numbers()
        display_analysis(numbers)

        again = input("\nAnalyze another dataset? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThank you for using Data Analyzer CLI. Goodbye!")
            break


if __name__ == "__main__":
    main()
