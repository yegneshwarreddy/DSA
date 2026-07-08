"""
Day 09 - Queue

Author: Yegneshwar

Goal:
    Learn Queue implementation and
    common interview problems.
"""

from collections import deque


class Queue:
    """
    Queue Implementation using collections.deque.
    """

    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        """
        Add an element to the rear.

        Time Complexity: O(1)
        """
        self.items.append(value)

    def dequeue(self):
        """
        Remove an element from the front.

        Time Complexity: O(1)
        """

        if self.is_empty():
            return None

        return self.items.popleft()

    def front(self):
        """
        Return the front element.

        Time Complexity: O(1)
        """

        if self.is_empty():
            return None

        return self.items[0]

    def rear(self):
        """
        Return the rear element.

        Time Complexity: O(1)
        """

        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        """
        Time Complexity: O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Time Complexity: O(1)
        """
        return len(self.items)


def generate_binary_numbers(n):
    """
    Generate binary numbers from 1 to n using Queue.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    result = []
    queue = deque(["1"])

    for _ in range(n):

        current = queue.popleft()

        result.append(current)

        queue.append(current + "0")
        queue.append(current + "1")

    return result


if __name__ == "__main__":

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front:", queue.front())

    print("Rear:", queue.rear())

    print("Dequeue:", queue.dequeue())

    print("Size:", queue.size())

    print("Is Empty:", queue.is_empty())

    print("Binary Numbers:", generate_binary_numbers(10))