.DEFAULT_GOAL := help

.PHONY: help
help: ## provides cli help for this make file (default)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: ci
ci: lint tests dist ## run continuous integration process on spike-starter
	@. venv/bin/activate; python -u -m unittest discover ${args} spike_starter_tests/continuous_integration

.PHONY: lint
lint: ## run static analysis on spike-starter
	@. venv/bin/activate; pylint --rcfile=.pylintrc spike_starter

.PHONY: dist
dist: ## build distribution archives
	@. venv/bin/activate; python setup.py sdist bdist_wheel

.PHONY: tests
tests: tests_integrations ## run automatic testing on spike-starter

.PHONY: tests_integrations
tests_integrations: ## run only integrations testing on spike-starter
	@. venv/bin/activate; python -u -m unittest discover ${args} spike_starter_tests/integrations

.PHONY: install
install: ## install python dependencies
	@. venv/bin/activate; pip install -e.[dev]

.PHONY: venv
venv: ## build virtualenv in ./venv directory and install python dependencies
	virtualenv -p python3 venv
	$(MAKE) install



