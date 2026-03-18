## Summary

Add a `hello.sh` Bash script to the repository root that prints `Hello, World!` to stdout. This is a greenfield addition to a minimal project that currently contains only a `README.md`. No existing scripts or utilities exist to reuse.

## Acceptance Criteria

- `hello.sh` exists at the repository root
- File begins with `#!/usr/bin/env bash` shebang line
- Running `./hello.sh` outputs exactly `Hello, World!` (with newline)
- File has executable permissions (`chmod +x`)

## Technical Approach

The project is a near-empty repository with only a `README.md` and `.ralph/` config directory. There are no existing shell scripts, utilities, or patterns to reuse.

The implementation is a single new file at the repository root:

```bash
#!/usr/bin/env bash
echo "Hello, World!"
```

Use `#!/usr/bin/env bash` over `#!/bin/bash` for portability across systems where Bash may not be at `/bin/bash` (e.g., NixOS, some macOS configurations).

## Files & Modules

| File | Action | Description |
|------|--------|-------------|
| `hello.sh` | **Create** | New executable Bash script at repo root |

No existing files are modified.

## Testing Strategy

1. **Permission check**: `test -x hello.sh` — verify executable bit is set
2. **Shebang check**: `head -1 hello.sh` — confirm it starts with `#!/usr/bin/env bash`
3. **Output check**: `./hello.sh` — confirm stdout is exactly `Hello, World!`
4. **Exit code check**: Verify the script exits with status `0`

Validation one-liner:
```bash
./hello.sh | diff - <(echo "Hello, World!") && echo "PASS" || echo "FAIL"
```

## Out of Scope

- Argument parsing or parameterized greetings
- Localization / i18n
- Integration with any build system or CI pipeline
- Adding tests to a test framework (none exists in this project)
- Modifications to `README.md`