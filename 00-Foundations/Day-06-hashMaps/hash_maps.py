"""
Day 06 - Hash Maps

Author: Yegneshwar

Goal:
    Learn how Hash Maps (Python dictionaries)
    solve common interview problems efficiently.
"""


def count_frequency(arr):
    """
    Count frequency of each element.

    Time: O(n)
    Space: O(n)
    """

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency


def first_non_repeating(text):
    """
    Return first non-repeating character.

    Time: O(n)
    Space: O(n)
    """

    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None


def two_sum(nums, target):
    """
    Return indices of two numbers whose sum equals target.

    Time: O(n)
    Space: O(n)
    """

    seen = {}

    for index, num in enumerate(nums):

        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []


def group_anagrams(words):
    """
    Group words that are anagrams.

    Time: O(n * k log k)
    Space: O(n)
    """

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        groups.setdefault(key, []).append(word)

    return list(groups.values())


if __name__ == "__main__":

    numbers = [1, 2, 2, 3, 4, 4, 4, 5]

    print("Frequency:", count_frequency(numbers))

    print("First Non-Repeating:", first_non_repeating("swiss"))

    print("Two Sum:", two_sum([2, 7, 11, 15], 9))

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("Anagrams:", group_anagrams(words))