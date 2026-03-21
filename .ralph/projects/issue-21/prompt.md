## Summary

Add a Python script `reverse.py` at the project root that reads a string from stdin and prints it reversed to stdout.

## Acceptance Criteria

- `reverse.py` exists at the project root
- Reading a line from stdin and printing the reversed string: `echo "hello" | python reverse.py` outputs `olleh`
- Handles empty input (prints empty line)
- Strips the trailing newline from input before reversing (does not reverse the newline character)

## Technical Approach

Since the project has no existing Python code or utilities, create a single standalone script using only the Python standard library.

- Use `input()` to read a line from stdin
- Use Python slice notation `[::-1]` to reverse the string
- Use `print()` to write the result to stdout

No dependencies, no classes, no abstractions — just a few lines of procedural code.

## Files & Modules

| Action | File | Description |
|--------|------|-------------|
| Create | `reverse.py` | Script that reads stdin and prints the reversed string |

## Testing Strategy

- **Manual verification**: `echo "hello" | python reverse.py` → `olleh`
- **Edge cases to verify**:
  - Empty string: `echo "" | python reverse.py` → empty line
  - Single character: `echo "a" | python reverse.py` → `a`
  - Palindrome: `echo "racecar" | python reverse.py` → `racecar`
  - Spaces: `echo "hello world" | python reverse.py` → `dlrow olleh`

## Out of Scope

- Multi-line input handling (only the first line is read)
- File input mode (only stdin)
- CLI argument parsing or flags
- Unicode normalization (grapheme clusters that span multiple code points)
- Installation packaging or `setup.py`