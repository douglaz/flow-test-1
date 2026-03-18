---
artifact: prompt-review
project: issue-5
backend: codex(gpt-5.4-xhigh)
role: prompt_reviewer
created_at: 2026-03-18T22:29:06Z
---

# Prompt Review

## Issues Found
- The expected CLI behavior is mostly clear, but output formatting is still slightly ambiguous: the prompt says “prints exactly” without explicitly stating whether the normal `print()` trailing newline is acceptable. Downstream loops often need that spelled out for strict verification.
- Extra positional arguments are mentioned only in “Out of Scope,” not in the core requirements. That leaves room for inconsistent implementations unless the prompt explicitly says to ignore all arguments after `sys.argv[1]`.
- The testing section includes a quoted multi-word argument case, but that case is not elevated into acceptance criteria. If it matters, it should be a required behavior, not just an example.
- The prompt implies Python usage but does not explicitly state Python 3. That usually works, but it is still a small source of avoidable ambiguity for execution and validation.
- “Only the `sys` stdlib module is imported” is clear in spirit, but should be stated as “no imports other than `sys`” to avoid interpretation gaps.
- The implementation guidance is slightly over-prescriptive (“No abstractions, classes, or helper functions are needed”). That is not harmful here, but requirements should focus on observable outcomes unless a specific structure is actually important.

## Refined Prompt
## Task

Create a new Python 3 CLI script named `greet.py` at the repository root.

The repository is otherwise empty except for an existing `README.md`. Do not modify any existing files.

## Required Behavior

The script must read command-line arguments using `sys.argv` only.

Behavior:
- If at least one positional argument is provided, use `sys.argv[1]` as the name.
- If no positional argument is provided, use `"World"` as the default name.
- Print exactly `Hello, {name}!` to standard output using Python’s normal `print()` behavior.
- Ignore any additional positional arguments beyond the first.

Examples:
- `python greet.py Alice` -> `Hello, Alice!`
- `python greet.py` -> `Hello, World!`
- `python greet.py "Bob Smith"` -> `Hello, Bob Smith!`

## Constraints

- Create exactly one new file: `greet.py`
- Place `greet.py` in the repository root
- Use only the Python standard library
- Do not import any module other than `sys`
- Do not use `argparse`, `click`, or any other argument-parsing library
- Keep the implementation self-contained in `greet.py`
- No test framework, packaging files, or additional project structure should be added

## Acceptance Criteria

The task is complete only if all of the following are true:
- `greet.py` exists at the repository root
- Running `python greet.py Alice` writes `Hello, Alice!` to stdout
- Running `python greet.py` writes `Hello, World!` to stdout
- Running `python greet.py "Bob Smith"` writes `Hello, Bob Smith!` to stdout
- The script uses `sys.argv` for argument parsing
- The script contains no imports other than `sys`
- No files other than `greet.py` are created or modified

## Implementation Notes

A simple top-level script is sufficient. A minimal implementation should:
1. `import sys`
2. Check `len(sys.argv)`
3. Use `sys.argv[1]` when present, otherwise `"World"`
4. Print `Hello, {name}!`

## Verification

Manually verify with:

```bash
python greet.py Alice
python greet.py
python greet.py "Bob Smith"
```

Expected stdout:
- `Hello, Alice!`
- `Hello, World!`
- `Hello, Bob Smith!`

## Out of Scope

- Supporting named flags such as `--name` or `--help`
- Validating or sanitizing input
- Handling multiple names beyond using only the first positional argument
- Adding automated tests
- Adding packaging or environment configuration files
