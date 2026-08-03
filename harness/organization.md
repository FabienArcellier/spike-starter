---
title: Organization
description: Repository organization, directory structure, module boundaries
order: 2
---

# Organization

```
<project-root>/
├── src/spike_starter/   # package source (src layout)
│   ├── __main__.py      # Click CLI entry point + main()
│   └── spike_starter.py # SpikeStarter class + _copytree()
├── scripts/             # deployment helpers
│   └── deploy_current_version.py
├── tests/               # external test package (src layout)
│   ├── units/           # unit tests (mock-based, no network/filesystem)
│   ├── integrations/    # integration tests (exercise the CLI)
│   ├── check/           # distribution sanity checks (run on built archives)
│   └── fixtures/
│       └── template_project/   # sample blueprint used by tests
├── pyproject.toml       # Poetry config + ruff config + alfred-cli dev dep
├── .alfred.toml         # alfred-cli project manifest (task runner)
├── alfred/              # alfred-cli task runner commands (ci.py, release.py)
└── .github/workflows/   # CI/CD pipeline (ci.yml runs `alfred ci`, cd.yml runs `alfred cd`)
```

## Key locations

- **CLI entry point**: `src/spike_starter/__main__.py:main()` — registered as `spike-starter` console script.
- **Core logic**: `src/spike_starter/spike_starter.py` — `SpikeStarter` handles project path generation, directory creation, git init, and template import (local or git).
- **Separate build vs source**: `src/` layout — tests live outside the package in `tests/`, packaged via `packages = [{ include = "spike_starter", from = "src" }]`.
- **Template ignore file**: a `.spikeignore` file (list of paths, one per line) controls what is copied from a blueprint; defaults to ignoring `.git`.