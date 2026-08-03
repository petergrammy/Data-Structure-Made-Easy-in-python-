# Hashing and Hash Tables

## Must know

- A hash code converts a key into an integer.
- A hash table uses that integer to choose where data may live.
- Collisions happen when different keys map to the same place.
- Python `dict` and `set` are hash-table based.
- Equal objects must have equal hashes.

## Python details

- Immutable built-ins like `str`, `int`, and `tuple` can usually be dictionary keys.
- Mutable objects like `list` cannot be dictionary keys.
- If you define `__eq__`, think carefully before defining `__hash__`.

## Implement

- A simple hash table using separate chaining.
- `put`, `get`, `remove`, and `resize`.

## Patterns

- Frequency counting.
- Membership checking.
- Deduplication.
- Grouping.
- Prefix-sum hash maps.

