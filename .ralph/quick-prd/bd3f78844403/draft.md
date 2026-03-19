## Summary

Add a `fib.py` file containing a `fibonacci(n)` function that returns the nth Fibonacci number, along with a `__main__` block that prints the result of `fibonacci(10)`.

## Acceptance Criteria

- A file `fib.py` exists at the repository root.
- `fibonacci(n)` returns the nth Fibonacci number (0-indexed: `fibonacci(0) = 0`, `fibonacci(1) = 1`, `fibonacci(10) = 55`).
- Running `python fib.py` prints the output of `fibonacci(10)` to stdout.
- The function handles `n = 0` and `n = 1` correctly.
- The function raises a `ValueError` for negative input.

## Technical Approach

- Use an iterative approach (simple loop) rather than recursion to avoid stack overflow on large `n` and to keep performance O(n) time / O(1) space.
- No external dependencies required — only Python standard library.
- No existing code in the repository to reuse; this is a new standalone file.

## Files & Modules

| File | Action | Description |
|------|--------|-------------|
| `fib.py` | Create | Contains `fibonacci(n)` function and `if __name__ == "__main__"` block |

## Testing Strategy

- Run `python fib.py` and verify the output is `55`.
- Spot-check known values: `fibonacci(0) == 0`, `fibonacci(1) == 1`, `fibonacci(5) == 5`, `fibonacci(10) == 55`.
- Verify `fibonacci(-1)` raises `ValueError`.

## Out of Scope

- Memoization or caching for repeated calls.
- CLI argument parsing (the main block hardcodes `n=10`).
- A separate test file or test framework setup.
- Type hints or packaging configuration.