"""
Day 03 - Strings

Author: Yegneshwar

Goal:
    Learn common string operations and
    understand their time complexities.
"""


def string_length(text):
    """O(1)"""
    return len(text)


def reverse_string(text):
    """O(n)"""
    return text[::-1]


def is_palindrome(text):
    """O(n)"""
    return text == text[::-1]


def count_vowels(text):
    """O(n)"""

    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    return count


def count_characters(text):
    """O(n)"""

    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    return frequency


def remove_spaces(text):
    """O(n)"""
    return text.replace(" ", "")


def uppercase_string(text):
    """O(n)"""
    return text.upper()


if __name__ == "__main__":

    sample = "Artificial Intelligence"

    print("Length:", string_length(sample))

    print("Reverse:", reverse_string(sample))

    print("Palindrome:", is_palindrome("madam"))

    print("Vowels:", count_vowels(sample))

    print("Character Frequency:", count_characters("banana"))

    print("Remove Spaces:", remove_spaces(sample))

    print("Uppercase:", uppercase_string(sample))