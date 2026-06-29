"""
Day 02 - Arrays

Author: Yegneshwar

Goal:
    Learn common array operations and
    understand their time complexities.
"""


def access_element(arr, index):
    """O(1)"""
    return arr[index]


def search_element(arr, target):
    """O(n)"""

    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1


def insert_end(arr, value):
    """Amortized O(1)"""

    arr.append(value)
    return arr


def insert_beginning(arr, value):
    """O(n)"""

    arr.insert(0, value)
    return arr


def delete_element(arr, target):
    """O(n)"""

    if target in arr:
        arr.remove(target)

    return arr


def reverse_array(arr):
    """O(n)"""

    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


def find_max(arr):
    """O(n)"""

    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum


if __name__ == "__main__":

    numbers = [10, 20, 30, 40, 50]

    print("Access:", access_element(numbers, 2))

    print("Search:", search_element(numbers, 40))

    print("Insert End:", insert_end(numbers.copy(), 60))

    print("Insert Beginning:", insert_beginning(numbers.copy(), 5))

    print("Delete:", delete_element(numbers.copy(), 30))

    print("Reverse:", reverse_array(numbers.copy()))

    print("Maximum:", find_max(numbers))