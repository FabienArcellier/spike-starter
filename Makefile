.DEFAULT_GOAL := help

.PHONY: ci
ci: lint tests dist ## run continuous integration process on spike-starter

.PHONY: cd
cd: _deploy_pypi ## run continuous deployment process on spike-starter

.PHONY: dist
dist: ## build distribution archives
	poetry build
	poetry run python -u -m unittest discover ${args} tests/continuous_integration

.PHONY: help
help: ## provides cli help for this make file (default)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: ## install python dependencies
	poetry install

.PHONY: lint
lint: ## run static analysis on spike-starter
	poetry run ruff check --config pyproject.toml src/spike_starter tests

.PHONY: deploy_current_version
deploy_current_version: install ## deploy the current spike-starter version through travis.ci
	poetry run python scripts/deploy_current_version.py

.PHONY: tests
tests: tests_units tests_integrations ## run automatic testing on spike-starter

.PHONY: tests_integrations
tests_integrations: ## run only integrations testing on spike-starter
	poetry run python -u -m unittest discover ${args} tests/integrations

.PHONY: tests_units
tests_units: ## run only units testing on spike-starter
	poetry run python -u -m unittest discover ${args} tests/units

# Private tasks

.PHONY: _deploy_pypi
_deploy_pypi: dist
	poetry publish