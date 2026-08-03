---
title: Python Alfred — alfred-cli task runner CI
description: alfred-cli is a task runner: commands declared in <project>/alfred/*.py
order: 4 
---

# Python Alfred — alfred-cli task runner CI

**alfred-cli** is a task runner: commands declared in `<project>/alfred/*.py`
expose the **continuous integration pipeline** of the project. The `ci` namespace drives
lint, formatting and tests through `alfred ci`, `alfred ci.lint`, `alfred ci.format` and
`alfred ci.tests`.

Each command is a function decorated with `@alfred.command("dotted.name", help=...)`.
`alfred-cli` is declared as a dev dependency in `pyproject.toml` so `import alfred`
resolves inside the subproject.

Reference API: <https://alfred-cli.readthedocs.io/en/latest/api_reference.html>

# Command namespace

Commands use a dotted namespace rooted at `ci`, matching their sub-project domain.

- `ci` — run the full CI pipeline (lint + format + tests)
- `ci.tests` — run all tests (unit + integration)
- `ci.tests.unit` / `ci.tests.integration` — run a single test suite
- `ci.lint` — run `ruff check`
- `ci.format` — check formatting with `ruff format --check`

## Composing commands

Composite commands orchestrate sub-commands in-process with `alfred.invoke_command`,
so each step runs in a clean isolated invocation.

```python
@alfred.command("ci", help="run the project CI (lint + format + tests)")
@alfred.option("--fix", is_flag=True, default=False, help="apply ruff fixes and formatting")
def ci(fix: bool):
    alfred.invoke_command("ci.lint", fix=fix)
    alfred.invoke_command("ci.format", fix=fix)
    alfred.invoke_command("ci.tests")
```

## Resolving and running tools

Resolve a binary with `alfred.sh("name", "fail message")` and run it with
`alfred.run(binary, args_list)`.

```python
ruff = alfred.sh("ruff", "ruff is missing")
alfred.run(ruff, ["check", "."])
```

Workflows can ignore errors by passing `exit_on_error=False` and hide output with
`stream_stdout=False`.

<HARD LIMIT>
- Always pass arguments as a list to `alfred.run(binary, args_list)`. Never build a
  shell string from user or variable input (shell injection risk).
</HARD LIMIT>

## --fix flag convention

Commands that can repair the tree expose a `--fix` boolean option. Boolean flags
must be declared as `is_flag=True, default=False`.

- `ci.lint --fix` runs `ruff check --fix .`; without the flag it runs `ruff check .`.
- `ci.format` checks formatting (`ruff format --check .`) by default; `--fix` applies it (`ruff format .`).
- `ci --fix` forwards the flag to both `ci.lint` and `ci.format`.

```python
@alfred.command("ci.format", help="check project formatting with ruff format")
@alfred.option(
    "--fix", is_flag=True, default=False, help="apply ruff formatting instead of checking"
)
def ci_format(fix: bool):
    ruff = alfred.sh("ruff", "ruff is missing")
    args = ["format", "."] if fix else ["format", "--check", "."]
    alfred.run(ruff, args)
```

## Working directory

When a command runs, alfred sets the working directory to the subproject root
(`<project>`), so relative paths such as `tests/units` resolve
against the subproject, not the repository root.