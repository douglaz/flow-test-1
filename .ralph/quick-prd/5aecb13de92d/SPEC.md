## Summary

Add a `greet.py` CLI script to the project root that prints a greeting. It accepts an optional positional name argument via `sys.argv` and defaults to "World". This is a greenfield addition to an otherwise empty repository (only `README.md` exists).

## Acceptance Criteria

- `greet.py` exists at the repository root
- `python greet.py Alice` prints exactly `Hello, Alice!` to stdout
- `python greet.py` (no args) prints exactly `Hello, World!` to stdout
- Argument parsing uses only `sys.argv` — no `argparse`, `click`, or other libraries
- No external dependencies; only the `sys` stdlib module is imported

## Technical Approach

The repository is empty (single `README.md`), so there is no existing code to reuse or integrate with. The implementation is a single self-contained script.

1. Import `sys`.
2. Read `sys.argv`: if `len(sys.argv) > 1`, use `sys.argv[1]` as the name; otherwise default to `"World"`.
3. Print `Hello, {name}!` to stdout via `print()`.

No abstractions, classes, or helper functions are needed — a top-level script body is sufficient.

## Files & Modules

| Action | Path | Purpose |
|--------|------|---------|
| **Create** | `greet.py` | CLI greeting script |

No existing files are modified.

## Testing Strategy

Manual verification (no test framework exists in the repo):

```bash
# With argument
python greet.py Alice
# Expected: Hello, Alice!

# Without argument
python greet.py
# Expected: Hello, World!

# With multi-word quoted argument (edge case)
python greet.py "Bob Smith"
# Expected: Hello, Bob Smith!
```

If a test framework is added later, a simple `subprocess.run` test asserting stdout output would cover all cases.

## Out of Scope

- Multiple positional arguments (only the first is used)
- Flag-style options (`--name`, `--help`)
- Input validation or error handling beyond the default behavior
- Adding a test framework or test files
- Packaging, `setup.py`, or `pyproject.toml`