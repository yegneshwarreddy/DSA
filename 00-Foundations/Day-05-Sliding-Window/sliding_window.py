"""
Day 05 - Sliding Window

Author: Yegneshwar

Goal:
    Learn the Sliding Window technique
    through common interview problems.
"""


def max_sum_subarray(arr, k):
    """
    Maximum sum of a subarray of size k.

    Time: O(n)
    Space: O(1)
    """

    if k > len(arr):
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum


def average_subarray(arr, k):
    """
    Average of every subarray of size k.

    Time: O(n)
    """

    averages = []

    window_sum = sum(arr[:k])
    averages.append(window_sum / k)

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        averages.append(window_sum / k)

    return averages


def longest_unique_substring(text):
    """
    Longest substring without repeating characters.

    Time: O(n)
    """

    left = 0
    seen = {}
    longest = 0

    for right, ch in enumerate(text):

        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        longest = max(longest, right - left + 1)

    return longest


def smallest_subarray_with_sum(arr, target):
    """
    Smallest subarray whose sum >= target.

    Time: O(n)
    """

    left = 0
    window_sum = 0
    minimum = float("inf")

    for right in range(len(arr)):

        window_sum += arr[right]

        while window_sum >= target:

            minimum = min(minimum, right - left + 1)

            window_sum -= arr[left]
            left += 1

    if minimum == float("inf"):
        return 0

    return minimum


if __name__ == "__main__":

    numbers = [2, 1, 5, 1, 3, 2]

    print("Max Sum:", max_sum_subarray(numbers, 3))

    print("Averages:", average_subarray(numbers, 3))

    print("Longest Unique:", longest_unique_substring("abcabcbb"))

    print("Smallest Length:", smallest_subarray_with_sum([2,1,5,2,3,2],7))