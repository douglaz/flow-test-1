## Summary

Add a standalone Python script `wordcount.py` to the repository root that reads text from stdin and prints the total word count to stdout. This is a simple utility with no dependencies beyond the Python standard library.

## Acceptance Criteria

- A file `wordcount.py` exists at the repository root.
- Running `echo "hello world" | python wordcount.py` prints `2`.
- Empty input prints `0`.
- Handles multiple lines of input, counting all words across lines.
- Handles multiple whitespace characters (tabs, multiple spaces, newlines) correctly by splitting on whitespace.
- Script is executable and includes a `#!/usr/bin/env python3` shebang.

## Technical Approach

- Use `sys.stdin.read()` to consume all of stdin.
- Use Python's built-in `str.split()` (no arguments) to split on arbitrary whitespace and count the resulting list length. This handles tabs, multiple spaces, and newlines without any special logic.
- Print the count via `print()`.
- Wrap execution in an `if __name__ == "__main__":` guard.
- No existing code in the repository to reuse — the project currently contains only `README.md`.

## Files & Modules

| File | Action | Description |
|---|---|---|
| `wordcount.py` | Create | New script: reads stdin, prints word count |

## Testing Strategy

- **Manual smoke tests:**
  - `echo "hello world" | python wordcount.py` → `2`
  - `printf "" | python wordcount.py` → `0`
  - `printf "one\ntwo three\n" | python wordcount.py` → `3`
  - `printf "  spaced   out  " | python wordcount.py` → `2`
- **Optional unit test:** If a test framework is added later, extract the counting logic into a function and test it directly with edge cases (empty string, only whitespace, unicode words).

## Out of Scope

- Character count, line count, or other `wc`-like features.
- File path arguments (only stdin is supported).
- Per-line or per-file breakdown.
- Third-party dependencies or packaging (setup.py, pyproject.toml).
- Locale-aware or language-specific word splitting.