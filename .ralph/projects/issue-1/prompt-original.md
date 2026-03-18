## Summary

Add a single-file Python script `hello.py` to the repository root that prints `Hello, World!` to stdout. The repository currently contains only a `README.md`; no existing code to integrate with or reuse.

## Acceptance Criteria

- [ ] `hello.py` exists at the repository root (`./hello.py`)
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
| Create | `./hello.py` | Single `print("Hello, World!")` statement |

## Testing Strategy

1. **Execution test:** Run `python hello.py`, capture stdout to a file, and verify both the exit code and the exact output bytes:
```sh
python hello.py > output.txt
test $? -eq 0 || echo "FAIL: non-zero exit code"
printf 'Hello, World!\n' > expected.txt
diff expected.txt output.txt || echo "FAIL: stdout mismatch"
rm -f output.txt expected.txt
```
This avoids command substitution (which strips trailing newlines) and explicitly asserts exit code 0 alongside a byte-exact stdout comparison.

2. **Content test:** Verify the file contains exactly one line: `print("Hello, World!")`.
```sh
diff <(cat hello.py) <(printf 'print("Hello, World!")\n') || echo "FAIL: file content mismatch"
```

## Out of Scope

- Adding a shebang line or making the file executable
- Adding `if __name__ == "__main__":` guard
- Adding type hints, docstrings, or comments
- Creating a test file or test framework setup
- Modifying `README.md` or any other existing file