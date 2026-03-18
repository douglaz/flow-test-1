---
artifact: prompt-review
project: issue-1
backend: codex(gpt-5.4-xhigh)
role: prompt_reviewer
created_at: 2026-03-18T21:37:12Z
---

# Prompt Review

## Issues Found
- The prompt does not say whether `stderr` must be empty. An implementation could meet the stdout check while still emitting warnings or errors.
- The validation examples use Bash-specific process substitution (`<(...)`). That is less portable and can fail in environments that execute tests with `sh`.
- The statement that the repository "currently contains only a `README.md`" is brittle project-state context, not a durable requirement. If the repo changes, that line becomes stale and can mislead downstream loops.
- The file-content constraint is expressed as several overlapping rules. Replacing that with one exact-content requirement is clearer and easier to test.
- The prompt assumes validation is run from the repository root with `python` on `PATH`, but it does not state those assumptions explicitly. That matters for repeatable execution.

## Refined Prompt
### Summary

Create a new file `hello.py` at the repository root. When run with `python hello.py` from the repository root, it must print `Hello, World!` to standard output and exit successfully.

### Deliverable

- Create exactly one new file: `./hello.py`

### Required File Content

`hello.py` must contain exactly this single line, followed by one final newline:

```python
print("Hello, World!")
```

### Constraints

- Do not add a shebang.
- Do not add comments, imports, functions, classes, or an `if __name__ == "__main__":` guard.
- Do not add leading or trailing whitespace.
- Do not add blank lines before or after the `print` statement.
- Do not create, modify, rename, or delete any file other than `./hello.py`.
- Do not rely on any existing project code or utilities.

### Acceptance Criteria

- `./hello.py` exists at the repository root.
- `./hello.py` is byte-for-byte equal to `print("Hello, World!")\n`.
- Running `python hello.py` from the repository root exits with status code `0`.
- Running `python hello.py` from the repository root writes exactly `Hello, World!\n` to stdout.
- Running `python hello.py` from the repository root writes nothing to stderr.

### Validation Steps

Run these commands from the repository root:

```sh
python hello.py > output.txt 2> stderr.txt
status=$?
printf 'Hello, World!\n' > expected_stdout.txt
printf 'print("Hello, World!")\n' > expected_file.txt

test "$status" -eq 0
cmp -s output.txt expected_stdout.txt
test ! -s stderr.txt
cmp -s hello.py expected_file.txt

rm -f output.txt stderr.txt expected_stdout.txt expected_file.txt
```

### Out of Scope

- Making `hello.py` executable
- Adding tests, CI configuration, or helper scripts
- Modifying `README.md` or any other existing file
