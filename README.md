# Spike starter

this tool allow to create a project prefix with the date and the time to
experiment.

```bash
# Simple usage
python -m spike-starter myproject
# This command will generate 20180410_0722-myproject
```

It allow to use an existing directory as a reference

```bash
# Generate a directory based on a template
python -m spike-starter --template ~/template/java myproject
python -m spike-starter -t ~/template/java myproject
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

### Validation

A pull request on Spike starter should pass the automatic tests.

```bash
make tests
```
