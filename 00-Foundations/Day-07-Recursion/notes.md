# Notes

Recursion is when a function calls itself.

Every recursive function has two parts.

1. Base Case

Stops recursion.

Example:

if n == 0:
    return

--------------------------------

2. Recursive Case

Calls itself with a smaller problem.

Example:

return n * factorial(n-1)

--------------------------------

Call Stack

factorial(4)

↓

factorial(3)

↓

factorial(2)

↓

factorial(1)

↓

Returns back

--------------------------------

Common Interview Problems

- Factorial
- Fibonacci
- Binary Search
- Tree Traversal
- DFS
- Backtracking

--------------------------------

Interview Tip

Whenever a problem can be broken into smaller identical subproblems,

Think:

 Recursion