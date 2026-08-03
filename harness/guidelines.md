---
title: Guidelines
description: Architecture rules, design charter, rules by namespace
order: 3
---

# Guidelines

## Code style

- **Indentation**: 2 spaces (`.editorconfig`). Tabs only for Makefiles (none currently).
- **Line length**: 100 characters (`[tool.ruff] line-length`).
- **Ruff governance**: lint scope is `E, F, W, I, UP` (`[tool.ruff.lint] select`).
- Prefer f-strings for formatting (project already uses them, e.g. project id generation).

## Architecture rules

- **CLI-only package**: `spike_starter` is a console tool (no web/server), a thin Click wrapper over the `SpikeStarter` domain class.
- **Separation**: `__main__.py` holds only CLI concerns (options, logging config, error handling to `sys.exit(1)`); domain logic lives in `spike_starter.py`.
- **No Proxy/import redirection**: import directly from the source module, e.g. `from spike_starter.spike_starter import SpikeStarter` (note: unit tests currently import from `__main__` — keep imports consistent with the source of truth `spike_starter.py`).

## Rules by namespace

- `src/spike_starter/` — source package; `from src` layout. Do not put tests here.
- `tests/units/` — fast, mock-based unit tests; mock git repo detection and `os.path` calls (see `_side_effect_in_git_repository`).
- `tests/integrations/` — exercise the real CLI end to end.
- `tests/check/` — verify built `dist/` archives post-build (renamed from `continuous_integration`); must run after `poetry build`.

## Behavioral rules

- **Always** add a new alfred command (units vs integrations vs check) rather than mixing test types, and compose it into `ci`.
- **Never** package `tests/` or `scripts/` into distribution archives (asserted in `tests/check/test_dist.py`).
- **Never** commit credentials — the project deploys to PyPI via tags; keep publishing isolated in `alfred cd`.

## Security

- No secrets in the repo; deployment secrets live in the CI environment, not in committed files.