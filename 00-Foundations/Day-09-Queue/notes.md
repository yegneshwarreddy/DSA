# Notes

Queue = First In First Out (FIFO)

Example

Enqueue

10

10 20

10 20 30

↓

Dequeue

10 removed first

--------------------------------

Common Operations

Enqueue

Dequeue

Front

Rear

isEmpty

Size

--------------------------------

Applications

- CPU Scheduling
- Printer Queue
- Task Scheduling
- Message Brokers
- BFS Traversal
- Producer-Consumer Pattern

--------------------------------

Python Queue

collections.deque

append()

popleft()

--------------------------------

Interview Clues

Whenever you hear

- Scheduling
- Processing in order
- BFS
- Level Order Traversal

Think

 Queue

--------------------------------

Complexities

Enqueue → O(1)

Dequeue → O(1)

Front → O(1)