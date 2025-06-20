"""
Basic Problem Solving with Python
Author: tania-tasru
GitHub: https://github.com/tania-tasru
Description:
    A collection of beginner-friendly Python functions demonstrating
    basic problem-solving techniques. Includes:
    - Leap year check
    - Word and vowel count
    - Duplicate removal from list
    - Fibonacci series generation
"""

# --------------------------
# Check if a year is a leap year
# --------------------------
def is_leap_year(year):
    """
    Check whether a given year is a leap year.

    Args:
        year (int): Year to check.

    Returns:
        str: Result stating whether it's a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a Leap year"
    else:
        return f"{year} is not a Leap year"

# --------------------------
# Count words in a sentence
# --------------------------
def word_count(text):
    """
    Count the number of words in the input text.

    Args:
        text (str): Input sentence.

    Returns:
        int: Number of words.
    """
    words = text.split()
    return len(words)

# --------------------------
# Count vowels in a sentence
# --------------------------
def count_vowels(sentence):
    """
    Count the number of vowels (both uppercase and lowercase) in the sentence.

    Args:
        sentence (str): Input sentence.

    Returns:
        int: Number of vowels.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels)

# --------------------------
# Remove duplicate items from a list
# --------------------------
def remove_duplicates(items):
    """
    Remove duplicate elements from a list.

    Args:
        items (list): List with possible duplicate elements.

    Returns:
        list: New list with unique values.
    """
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

# --------------------------
# Generate Fibonacci series up to Nth term
# --------------------------
def fibonacci_series(n):
    """
    Generate the Fibonacci series up to the nth term (0-based index).

    Args:
        n (int): The index up to which the Fibonacci series will be generated.

    Returns:
        list: List containing the Fibonacci series.
    """
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    fibo = [0, 1]
    for i in range(2, n + 1):
        next_fibo = fibo[i - 1] + fibo[i - 2]
        fibo.append(next_fibo)
    return fibo

# --------------------------
# Run examples
# --------------------------
if __name__ == "__main__":
    # Leap Year Check
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        print(is_leap_year(year))
    except ValueError:
        print("Invalid input. Please enter a valid year.")

    # Word Count Example
    text = "I will call you later"
    print("\nText:", text)
    print("Word Count:", word_count(text))

    # Vowel Count Example
    sentence = "This is none of your business"
    print("\nSentence:", sentence)
    print("Vowel Count:", count_vowels(sentence))

    # Remove Duplicates Example
    numbers = [2, 2, 7, 7, 7, 8, 1, 2, 4, 10, 33, 33, 56, 70, 33]
    print("\nOriginal List:", numbers)
    print("Unique Numbers:", remove_duplicates(numbers))

    # Fibonacci Series Example
    print("\nFibonacci Series (first 10 terms):", fibonacci_series(9))