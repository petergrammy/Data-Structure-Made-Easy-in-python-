# Big-O

## Must know

- Big-O describes how work grows as input grows.
- Drop constants and lower-order terms.
- Worst case is the default unless stated otherwise.
- Amortized cost matters for dynamic arrays and hash tables.

## Common growth rates

- `O(1)`: dictionary lookup average case, list indexing.
- `O(log n)`: binary search, balanced-tree search.
- `O(n)`: scanning a list.
- `O(n log n)`: efficient comparison sorting.
- `O(n^2)`: many nested-loop pair checks.
- `O(2^n)`: brute-force subsets.

## Exercises

- Analyze 10 small functions by hand.
- Make a Big-O table for Python `list`, `dict`, `set`, and `deque`.
- Rewrite one `O(n^2)` solution using a hash table.

