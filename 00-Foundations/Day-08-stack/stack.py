"""
Day 08 - Stack

Author: Yegneshwar

Goal:
    Learn Stack implementation and
    common interview problems.
"""


class Stack:
    """
    Stack Implementation using Python List.
    """

    def __init__(self):
        self.items = []

    def push(self, value):
        """
        Time Complexity: O(1)
        """
        self.items.append(value)

    def pop(self):
        """
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        """
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


def is_valid_parentheses(text):
    """
    Check whether parentheses are balanced.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for ch in text:

        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":

            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


def reverse_string(text):
    """
    Reverse string using Stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    stack = list(text)

    result = ""

    while stack:
        result += stack.pop()

    return result


if __name__ == "__main__":

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Peek:", stack.peek())

    print("Pop:", stack.pop())

    print("Size:", stack.size())

    print("Empty:", stack.is_empty())

    print("Balanced:", is_valid_parentheses("{[()]}"))

    print("Reverse:", reverse_string("Python"))