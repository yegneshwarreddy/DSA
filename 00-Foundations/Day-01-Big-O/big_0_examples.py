"""
Day 01 - Time Complexity Examples

Author: Yegneshwar
Goal:
    Understand different time complexities by implementing
    simple examples.

"""


def constant_time(arr):
    """O(1)"""
    return arr[0]


def linear_time(arr):
    """O(n)"""
    total = 0

    for num in arr:
        total += num

    return total


def quadratic_time(arr):
    """O(n²)"""
    pairs = []

    for i in arr:
        for j in arr:
            pairs.append((i, j))

    return pairs


def logarithmic_time(arr, target):
    """O(log n) - Binary Search"""

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def linearithmic_time(arr):
    """O(n log n)"""
    return sorted(arr)


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("O(1):", constant_time(numbers))

    print("O(n):", linear_time(numbers))

    print("O(log n):", logarithmic_time(numbers, 7))

    print("O(n log n):", linearithmic_time(numbers[::-1]))

    print("O(n²) Pair Count:", len(quadratic_time([1, 2, 3])))