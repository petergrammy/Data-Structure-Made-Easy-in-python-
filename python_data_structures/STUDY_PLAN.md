# Study Plan

This plan assumes 10 weeks of steady preparation before or during the semester. If your course moves faster, compress the practice days first, not the implementation days.

## Daily routine

- 20 minutes: read or review one concept.
- 40 minutes: implement or trace examples by hand.
- 40 minutes: solve problems.
- 10 minutes: update `13_practice_problems/problem_log.md`.

## Week 1: Foundations and Big-O

Goals:
- Understand Big-O, Big-Omega, Big-Theta at a practical level.
- Recognize constant, logarithmic, linear, linearithmic, quadratic, and exponential growth.
- Know the cost of common Python operations on `list`, `dict`, `set`, `tuple`, and `deque`.

Practice:
- Analyze nested loops.
- Compare list search vs dictionary lookup.
- Time small snippets with `timeit`.

## Week 2: Python Collections and Arrays/Lists

Goals:
- Treat Python `list` as a dynamic array.
- Understand indexing, appending, inserting, deleting, slicing, and copying.
- Know when `array`, `list`, `tuple`, and `deque` make sense.

Practice:
- Implement a simplified dynamic array.
- Solve two-pointer and sliding-window problems.
- Reimplement common list operations manually.

## Week 3: Linked Lists

Goals:
- Understand nodes and references.
- Implement singly linked list operations.
- Understand dummy nodes, slow/fast pointers, and reversal.

Practice:
- Reverse a linked list.
- Detect a cycle.
- Merge two sorted linked lists.
- Remove the nth node from the end.

## Week 4: Stacks, Queues, and Deques

Goals:
- Know stack LIFO and queue FIFO behavior.
- Use `list` for simple stacks and `collections.deque` for queues.
- Recognize monotonic stack and monotonic queue patterns.

Practice:
- Balanced parentheses.
- Evaluate postfix expressions.
- Next greater element.
- Sliding window maximum.

## Week 5: Hashing, Dictionaries, and Sets

Goals:
- Understand hash codes, equality, collisions, and load factor.
- Use `dict`, `set`, `defaultdict`, and `Counter` fluently.
- Know how custom objects behave with `__eq__` and `__hash__`.

Practice:
- Two sum.
- Group anagrams.
- First unique character.
- Implement a simple hash table with chaining.

## Week 6: Recursion and Divide and Conquer

Goals:
- Build comfort with base cases and recursive progress.
- Trace recursive calls without getting lost.
- Convert simple recursive solutions to iterative ones when useful.

Practice:
- Factorial, Fibonacci, binary search.
- Generate subsets and permutations.
- Merge sort.
- Tree traversal previews.

## Week 7: Trees

Goals:
- Understand binary trees, binary search trees, and traversal orders.
- Use recursion naturally on trees.
- Know height, depth, balance, and subtree ideas.

Practice:
- Inorder, preorder, postorder, and level-order traversal.
- Validate a BST.
- Find lowest common ancestor.
- Compute tree height and diameter.

## Week 8: Heaps and Priority Queues

Goals:
- Understand heap shape and heap order.
- Use Python's `heapq`.
- Know when a priority queue beats sorting every time.

Practice:
- Top k frequent elements.
- Kth largest element.
- Merge k sorted lists.
- Task scheduling with priorities.

## Week 9: Graphs

Goals:
- Represent graphs with adjacency lists and matrices.
- Use BFS for shortest unweighted paths.
- Use DFS for traversal, components, and cycle detection.

Practice:
- Number of connected components.
- Shortest path in an unweighted graph.
- Topological sort.
- Dijkstra's algorithm with `heapq`.

## Week 10: Sorting, Searching, and Dynamic Programming

Goals:
- Know insertion sort, merge sort, quicksort, heap sort, and Python's Timsort at a conceptual level.
- Master binary search patterns.
- Understand memoization and tabulation.

Practice:
- Binary search on answer.
- Merge intervals.
- Coin change.
- Longest increasing subsequence.
- 0/1 knapsack.

## Exam preparation loop

Before an exam, make one page per topic:

- Definition.
- Supported operations.
- Big-O table.
- One clean implementation.
- Three common problem patterns.
- Mistakes you personally make.

