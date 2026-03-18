## Summary

Create a new file `hello.txt` in the project root containing the text `Hello, World!` on a single line. This is a minimal addition to the repository with no dependencies on existing code.

## Acceptance Criteria

- A file named `hello.txt` exists at the repository root (`/`).
- The file contains exactly one line: `Hello, World!`
- The file uses a trailing newline (standard POSIX text file convention).
- No existing files are modified.

## Technical Approach

The project root currently contains only `README.md`. Create `hello.txt` as a new plain-text file alongside it. No existing utilities, templates, or abstractions are involved — this is a standalone static file.

## Files & Modules

| Action | Path | Description |
|--------|------|-------------|
| **Create** | `hello.txt` | New file with content `Hello, World!\n` |

## Testing Strategy

- Verify the file exists at the repository root.
- Verify the file content is exactly `Hello, World!` followed by a newline.
- Verify no other files were modified (`git diff` shows only the new file).

## Out of Scope

- Localization or parameterized content.
- Build system or CI integration for this file.
- Any changes to existing files (`README.md`, `.ralph/` configuration).