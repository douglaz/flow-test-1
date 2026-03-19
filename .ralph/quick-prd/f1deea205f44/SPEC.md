## Summary

Add a `goodbye.txt` file to the project root containing the text `Goodbye, World!` on a single line. This is a straightforward file creation with no dependencies on existing code.

## Acceptance Criteria

- A file named `goodbye.txt` exists at the project root.
- The file contains exactly one line: `Goodbye, World!`
- No other files are modified.

## Technical Approach

The project is a minimal repository with only a `README.md` at the root. There is no existing code, build system, or utilities to reuse. The change is a single new file creation.

1. Create `goodbye.txt` in the project root with the content `Goodbye, World!\n`.

## Files & Modules

| Action | Path | Description |
|--------|------|-------------|
| Create | `goodbye.txt` | New file with `Goodbye, World!` content |

## Testing Strategy

- Verify `goodbye.txt` exists at the project root.
- Verify the file content is exactly `Goodbye, World!` followed by a newline.
- Verify no other files were modified (`git diff` shows no unrelated changes).

## Out of Scope

- Modifications to `README.md` or any other existing files.
- Any build, CI, or automation changes.
- Localization or parameterization of the message.