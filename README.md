# Spike starter

[![Build Status](https://travis-ci.org/FabienArcellier/spike-starter.svg?branch=master)](https://travis-ci.org/FabienArcellier/spike-starter)

this tool allow to create a project prefix with the date and the time to
experiment.

```bash
# Simple usage
python -m spike-starter myproject
# This command will generate 20180410_0722__myproject
```

It allow to use an existing directory as a reference

```bash
# Generate a directory based on a template
python -m spike-starter --template ~/template/java myproject
python -m spike-starter -t ~/template/java myproject
```

## Usage with alias

An alias can be use to generate a spike based on a specific stack.

```bash
alias spike-starter-python='spike-starter -t ~/projects/0004-spikes_template/python_spike'
alias spike-starter-python3='spike-starter -t ~/projects/0004-spikes_template/python3_spike'
```

## Installation

after the installation, the command `spike_starter` can be used from anywhere on your
system.

1. install with pip

```bash
git clone https://github.com/FabienArcellier/spike-starter.git
cd spike-starter
pip install .
```

## Contribute

### Continuous integration process

A pull request must pass the continuous integration process
to be merged on ``master``.

```bash
make ci
```

### Continuous deployment process

The automation task ``make deploy_current_version`` will trigger a deployment
based on tag generation.

Travis.ci will deploy the current tagged version on PyPi.

### List automation tasks

```
$make

cd                             run continuous deployment process on spike-starter
ci                             run continuous integration process on spike-starter
deploy_current_version         deploy the current spike-starter version through travis.ci
dist                           build distribution archives
help                           provides cli help for this make file (default)
install                        install python dependencies
lint                           run static analysis on spike-starter
tests_integrations             run only integrations testing on spike-starter
tests                          run automatic testing on spike-starter
venv                           build virtualenv in ./venv directory and install python dependencies
```
