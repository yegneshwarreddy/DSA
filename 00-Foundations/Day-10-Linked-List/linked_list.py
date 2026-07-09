"""
Day 10 - Linked List

Author: Yegneshwar

Goal:
    Learn Singly Linked List implementation and
    common operations.
"""


class Node:
    """
    Represents a single node in a Linked List.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """
        Time Complexity: O(n)
        """

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_beginning(self, data):
        """
        Time Complexity: O(1)
        """

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def delete(self, key):
        """
        Delete first occurrence.

        Time Complexity: O(n)
        """

        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:
            return

        previous.next = current.next

    def search(self, key):
        """
        Time Complexity: O(n)
        """

        current = self.head

        while current:

            if current.data == key:
                return True

            current = current.next

        return False

    def display(self):
        """
        Time Complexity: O(n)
        """

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


if __name__ == "__main__":

    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    ll.insert_at_beginning(5)

    ll.display()

    print("Search 20:", ll.search(20))

    ll.delete(20)

    ll.display()