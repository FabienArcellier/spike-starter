.DEFAULT_GOAL := help

.PHONY: help
help: ## provides cli help for this make file (default)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint: ## provides cli help for this make file (default)
	@. venv/bin/activate; pylint --rcfile=.pylintrc spike_starter


.PHONY: tests
tests: tests_integrations ## run all validation tests

.PHONY: tests_integrations
tests_integrations: ## run integrations tests
	@. venv/bin/activate; python -u -m unittest discover ${args} spike_starter_tests/integrations

.PHONY: venv
venv: ## generate python 2.7 virtualenv in venv directory
	virtualenv venv
	@. venv/bin/activate; pip install .
