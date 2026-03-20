## Summary

Add a standalone Python script `is_prime.py` to the project root that provides a primality-checking function and prints results for integers 1 through 20 when run directly.

## Acceptance Criteria

- A file `is_prime.py` exists at the project root.
- It defines a function `is_prime(n: int) -> bool` that returns `True` if `n` is prime, `False` otherwise.
- Edge cases handled: `n <= 1` returns `False`; `n == 2` returns `True`; even numbers > 2 return `False`.
- A `if __name__ == "__main__"` block prints the result of `is_prime(n)` for each `n` in 1–20, one per line (e.g., `1: False`, `2: True`, …).
- Running `python is_prime.py` produces correct output with no errors on Python 3.8+.

## Technical Approach

- Use trial division up to `√n` — the simplest correct algorithm with no dependencies.
- Short-circuit on `n <= 1`, `n == 2`, and even `n` before entering the loop.
- Iterate only over odd divisors from 3 to `√n` (step 2) for efficiency.
- No external libraries required; only `math.isqrt` (stdlib, Python 3.8+).
- No existing code in the repo to reuse — this is the first source file.

## Files & Modules

| Action | Path | Description |
|--------|------|-------------|
| Create | `is_prime.py` | Contains `is_prime()` function and `__main__` block |

## Testing Strategy

- **Manual verification**: Run `python is_prime.py` and confirm output matches known primes in 1–20 (2, 3, 5, 7, 11, 13, 17, 19).
- **Unit tests** (if a test framework is added later): test `is_prime` against edge cases (`0`, `1`, `2`, `-1`), small primes, small composites, and a larger prime (e.g., `97`).

## Out of Scope

- Performance optimization for very large numbers (Miller-Rabin, sieve).
- CLI argument parsing or interactive input.
- Adding a test framework or CI pipeline.
- Package structure (`setup.py`, `pyproject.toml`).