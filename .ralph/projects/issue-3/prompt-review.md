---
artifact: prompt-review
project: issue-3
backend: codex(gpt-5.4-xhigh)
role: prompt_reviewer
created_at: 2026-03-18T22:02:43Z
---

Reviewing the prompt for execution gaps and verification ambiguity. I’m focusing on places where an implementation loop could succeed locally but still miss the acceptance criteria, especially around Git mode tracking and exact output.
# Prompt Review

## Issues Found
- The Git permission requirement is underspecified. The prompt requires `hello.sh` to be tracked as `100755`, but it never explicitly requires `git add hello.sh` or `git add --chmod=+x hello.sh`, so an implementation loop could satisfy the filesystem check and still fail the Git metadata check.
- The intended file contents are shown as an example rather than stated as the exact deliverable. That leaves room for unnecessary variation such as extra comments, `set -e`, or `echo -n`.
- The execution contract is slightly incomplete. The prompt specifies exact stdout and exit status `0`, but it does not explicitly say the script must produce no stderr output.
- The environment assumptions are implicit. This task depends on a Unix-like environment with Bash, executable permission bits, and Git mode tracking; stating that directly improves feasibility and reduces confusion.
- File format details are omitted. Specifying LF line endings and plain ASCII makes the script more deterministic and avoids avoidable CRLF-related issues.

## Refined Prompt
Create a new executable Bash script named `hello.sh` at the repository root. This is a greenfield change. The repository currently contains `README.md` and `.ralph/` metadata only. Do not modify any existing file, and do not create any file other than `hello.sh`.

Use this exact file content:

```bash
#!/usr/bin/env bash
printf 'Hello, World!\n'
```

Requirements:
- `hello.sh` must exist at `./hello.sh`
- The first line must be exactly `#!/usr/bin/env bash`
- The file must use LF line endings and plain ASCII text
- Running `./hello.sh` from the repository root must write exactly `Hello, World!` followed by a single newline to stdout
- The script must exit with status `0`
- The script must not write anything to stderr
- The file must be executable on disk
- Git must track `hello.sh` in the index with mode `100755`

Implementation notes:
- After creating the file, ensure the executable bit is set and recorded in Git. Use either `chmod +x hello.sh && git add hello.sh` or `git add --chmod=+x hello.sh`
- Do not modify `README.md`, anything under `.ralph/`, or any other existing file
- Do not add tests, CI configuration, argument parsing, localization, or any additional scripts

Verification steps:
1. `test -x hello.sh`
2. `head -1 hello.sh | diff -u - <(printf '#!/usr/bin/env bash\n')`
3. `./hello.sh | diff -u - <(printf 'Hello, World!\n')`
4. `./hello.sh >/dev/null; test "$?" -eq 0`
5. `stderr="$(./hello.sh 2>&1 >/dev/null)"; test -z "$stderr"`
6. `git ls-files -s hello.sh | grep -Eq '^100755 '`

Task is complete only when all verification commands pass from the repository root.
