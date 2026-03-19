## Summary

Create a new file `fortune.txt` at the project root containing a single line of text: `The best time to plant a tree was 20 years ago.`

This is a minimal project — the repository contains only a `README.md` and configuration files. No existing utilities or patterns are relevant to this feature.

## Acceptance Criteria

- A file named `fortune.txt` exists at the repository root.
- The file contains exactly one line: `The best time to plant a tree was 20 years ago.`
- The file ends with a trailing newline (standard POSIX text file convention).

## Technical Approach

Create the file directly. The project has no build system, templating, or file-generation utilities to reuse. A single file write is the complete implementation.

## Files & Modules

| Action | File |
|--------|------|
| Create | `fortune.txt` |

No existing files are modified.

## Testing Strategy

- Verify `fortune.txt` exists at the repository root.
- Verify its content is exactly `The best time to plant a tree was 20 years ago.\n` (single line with trailing newline).
- No automated test framework exists in this project; manual inspection or a simple shell assertion (`diff` or `cat`) suffices.

## Out of Scope

- Adding multiple fortunes or a random-selection mechanism.
- Integrating fortune display into any build or runtime process.
- Creating a test framework for the project.