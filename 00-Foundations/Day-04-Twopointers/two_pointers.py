"""
Day 04 - Two Pointers

Author: Yegneshwar

Goal:
    Learn the Two Pointers technique
    through common interview problems.
"""


def reverse_array(arr):
    """
    Reverse an array in-place.
    Time: O(n)
    Space: O(1)
    """

    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def is_palindrome(text):
    """
    Check if a string is a palindrome.
    Time: O(n)
    Space: O(1)
    """

    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


def two_sum_sorted(arr, target):
    """
    Find two numbers whose sum equals target.
    Array must be sorted.

    Time: O(n)
    Space: O(1)
    """

    left = 0
    right = len(arr) - 1

    while left < right:

        current = arr[left] + arr[right]

        if current == target:
            return left, right

        elif current < target:
            left += 1

        else:
            right -= 1

    return -1


def remove_duplicates(arr):
    """
    Remove duplicates from sorted array.

    Returns new length.

    Time: O(n)
    Space: O(1)
    """

    if not arr:
        return 0

    slow = 0

    for fast in range(1, len(arr)):

        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    print("Reverse:", reverse_array(numbers.copy()))

    print("Palindrome:", is_palindrome("madam"))

    print("Two Sum:", two_sum_sorted([1, 2, 4, 6, 8, 10], 10))

    arr = [1, 1, 2, 2, 3, 4, 4]

    length = remove_duplicates(arr)

    print("Unique Length:", length)

    print("Unique Elements:", arr[:length])