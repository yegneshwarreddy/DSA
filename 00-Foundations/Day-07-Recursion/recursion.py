"""
Day 07 - Recursion

Author: Yegneshwar

Goal:
    Learn recursion by solving classic recursive problems.
"""


def factorial(n):
    """
    Calculate factorial using recursion.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """
    Return nth Fibonacci number.

    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_numbers(n):
    """
    Sum numbers from 1 to n.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if n == 1:
        return 1

    return n + sum_of_numbers(n - 1)


def reverse_string(text):
    """
    Reverse a string recursively.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


def binary_search(arr, target, left, right):
    """
    Recursive Binary Search.

    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)

    return binary_search(arr, target, left, mid - 1)


if __name__ == "__main__":

    print("Factorial:", factorial(5))

    print("Fibonacci:", fibonacci(8))

    print("Sum:", sum_of_numbers(10))

    print("Reverse:", reverse_string("Python"))

    numbers = [2, 4, 6, 8, 10, 12, 14]

    print("Binary Search:", binary_search(numbers, 10, 0, len(numbers)-1))