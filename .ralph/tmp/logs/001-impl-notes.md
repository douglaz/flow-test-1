# Implementation Notes

## Decisions Made
- Kept the script minimal (6 lines) since the spec is straightforward and no additional abstraction is needed
- Used `text.split()` directly inside `len()` rather than extracting a separate function, as the spec doesn't require unit-testable extraction and YAGNI applies

## Spec Deviations
- None — all acceptance criteria implemented exactly as specified

## Testing
- All four smoke tests from the acceptance criteria pass:
  - `echo "hello world" | python3 wordcount.py` → `2`
  - `printf "" | python3 wordcount.py` → `0`
  - `printf "one\ntwo three\n" | python3 wordcount.py` → `3`
  - `printf "  spaced   out  " | python3 wordcount.py` → `2`
- Shebang is `#!/usr/bin/env python3` (first line)
- File permissions are `-rwxr-xr-x` (executable)
- Execution is wrapped in `if __name__ == "__main__":` guard
- Counting logic uses `sys.stdin.read()` and `str.split()` with no arguments
