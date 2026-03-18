## Summary

Add a single-file Python script `hello.py` to the repository root that prints `Hello, World!` to stdout. The repository currently contains only a `README.md`; no existing code to integrate with or reuse.

## Acceptance Criteria

- [ ] `hello.py` exists at the repository root (`/`)
- [ ] Running `python hello.py` prints exactly `Hello, World!` to stdout (exit code 0)
- [ ] File contains only the `print` statement — no shebang, no comments, no imports, no functions, no trailing blank lines beyond the final newline

## Technical Approach

Create a new file `hello.py` at the repository root with the single line:

```python
print("Hello, World!")
```

No existing code, utilities, or patterns exist in this repository to reuse — the repo contains only `README.md`.

## Files & Modules

| Action | Path | Description |
|--------|------|-------------|
| Create | `hello.py` | Single `print("Hello, World!")` statement |

## Testing Strategy

1. **Execution test:** Run `python hello.py` and assert stdout is exactly `Hello, World!\n` with exit code 0.
2. **Content test:** Verify the file contains exactly one line: `print("Hello, World!")`.

No test framework is needed; a single shell command validates both criteria:
```sh
test "$(python hello.py)" = "Hello, World!"
```

## Out of Scope

- Adding a shebang line or making the file executable
- Adding `if __name__ == "__main__":` guard
- Adding type hints, docstrings, or comments
- Creating a test file or test framework setup
- Modifying `README.md` or any other existing file