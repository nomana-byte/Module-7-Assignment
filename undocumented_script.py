
"""
A program for processing numbers and strings.
"""


def process_numbers(numbers):
    """Double even numbers and triple odd numbers.

    Args:
        numbers: A list of integers.

    Returns:
        A list containing the processed integers.
    """
    return [
        number * 2 if number % 2 == 0 else number * 3
        for number in numbers
    ]


def process_strings(strings):
    """Change each string's case based on its length.

    Strings longer than five characters become uppercase.
    Other strings become lowercase.

    Args:
        strings: A list of strings.

    Returns:
        A string containing the processed words separated by spaces.
    """
    return " ".join(
        word.upper() if len(word) > 5 else word.lower()
        for word in strings
    )


def main():
    """Run the processing functions and display their results."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    strings = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(strings)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
