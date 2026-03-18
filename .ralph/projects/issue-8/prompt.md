## Summary

Add a `hello.txt` file to the project root containing the text `Hello, World!` on a single line. This is a straightforward file-creation task with no dependencies on existing code.

## Acceptance Criteria

- A file named `hello.txt` exists at the project root.
- The file contains exactly one line: `Hello, World!`
- The file uses a trailing newline (standard POSIX text file convention).

## Technical Approach

Create `hello.txt` in the repository root (`/`) alongside the existing `README.md`. No existing code or utilities need to be reused — this is a static content file with no logic.

## Files & Modules

| Action | Path | Description |
|--------|------|-------------|
| Create | `hello.txt` | New file with `Hello, World!` content |

No existing files are modified.

## Testing Strategy

- Verify the file exists at the project root.
- Verify the file content is exactly `Hello, World!\n` (single line, trailing newline).

## Out of Scope

- Dynamic content generation or templating.
- Localization or multi-language support.
- Integration with any build system or CI pipeline.