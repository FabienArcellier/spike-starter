---
title: Technology
description: Technology stack, tooling, build/test/lint commands
order: 1
---

# Technology

- **Language**: Python ^3.12
- **Package manager**: Poetry (layout `src/`, build backend `poetry-core`)
- **CLI framework**: Click
- **Git interaction**: GitPython
- **Linting + formatting**: Ruff (select `E,F,W,I,UP`, `line-length = 100`, `target-version = py312`)
- **Testing**: unittest (standard library), no pytest
- **Distribution**: Poetry build; `twine` for publishing
- **CI/CD**: GitHub Actions (`.github/workflows/ci.yml` + `cd.yml`)
- **Task runner**: alfred-cli (`alfred ci`, `alfred cd`, ...)

## Commands

```bash
poetry install                    # install dependencies (alfred install)
poetry run ruff check --config pyproject.toml src/spike_starter tests   # lint (alfred ci.lint)
poetry run python -u -m unittest discover tests/units         # unit tests (alfred ci.tests.unit)
poetry run python -u -m unittest discover tests/integrations  # integration tests (alfred ci.tests.integration)
poetry build                      # build dist archives (alfred dist)
poetry publish                    # publish to PyPI (alfred cd)
```

Alfred commands: `alfred ci` (lint + format + tests + dist), `alfred cd` (deploy), `alfred ci.tests` (units + integrations), `alfred install`, `alfred deploy_current_version` (creates and pushes the `v*` tag). The `--fix` flag applies ruff fixes/formatting.

## Runtime deps (`[tool.poetry.dependencies]`)

- `click`, `decorator`, `GitPython`

## Dev deps (`[tool.poetry.group.dev.dependencies]`)

- `alfred-cli`, `ruff`, `tox`, `twine`