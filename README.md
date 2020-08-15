# Spike-starter

[![Build Status](https://travis-ci.org/FabienArcellier/spike-starter.svg?branch=master)](https://travis-ci.org/FabienArcellier/spike-starter)

spike-starter creates project from blueprint template
and helps me on my experimentation workflow.

```bash
# Simple usage
spike-starter myproject
# This command will generate 20180410_0722__myproject
```

It will create a `Spike directory` :

* the name of the `Spike directory` is automatically prefix with date and time
to allow quick classification of experiments.

* the `Spike directory` is initialized as git repository

The term Spikes has been coined by [Kent Beck](https://fr.wikipedia.org/wiki/Kent_Beck) in Extreme Programming (XP).
It's a special type of story that is used to gain the knowledge
necessary to reduce the risk of a technical approach.

## Features

* usage
* local blueprint
* remote git blueprint

### usage

```bash
Usage: spike-starter [OPTIONS] [PROJECT_NAMES]...

  instanciate a project based on a project blueprint

Options:
  -t, --template TEXT  template path either local or git path
  -d, --debug          show debug information
  -v, --version        show version number
  --noprefix           instanciate a blueprint without date time prefix
  --help               Show this message and exit.
```

### local blueprint

It allow to use an existing directory as a reference.

```bash
# Generate a directory based on a template
spike-starter --template ~/template/java myproject
spike-starter -t ~/template/java myproject
```

### remote git blueprint

It can use remote git repository as template. The blueprint is cloned in local
and a new repository is iniated inside.

```bash
# Generate a directory based on a template
spike-starter --template https://github.com/FabienArcellier/blueprint-webapp-flask.git myproject
```

## Blueprints

* [FabienArcellier/blueprint-cli-multicommands-python](https://github.com/FabienArcellier/blueprint-cli-multicommands-python) : `spike-starter --template https://github.com/FabienArcellier/blueprint-cli-multicommands-python.git myproject`
* [FabienArcellier/blueprint-webapp-bootstrap](https://github.com/FabienArcellier/blueprint-webapp-bootstrap) : `spike-starter --template https://github.com/FabienArcellier/blueprint-webapp-bootstrap.git myproject`
* [FabienArcellier/blueprint-webapp-flask](https://github.com/FabienArcellier/blueprint-webapp-flask) : `spike-starter --template https://github.com/FabienArcellier/blueprint-webapp-flask.git myproject`
* [FabienArcellier/blueprint-webapp-flask-bootstrap](https://github.com/FabienArcellier/blueprint-webapp-flask-bootstrap) : `spike-starter --template https://github.com/FabienArcellier/blueprint-webapp-flask-bootstrap.git myproject`

* [FabienArcellier/blueprint-library-pip](https://github.com/FabienArcellier/blueprint-library-pip) : `spike-starter --template https://github.com/FabienArcellier/blueprint-library-pip myproject`


## Advanced usage

### Use aliases to have shortcuts to your favorite blueprints

An [alias](https://ss64.com/bash/alias.html) may be use to generate
a spike based on a specific blueprint already on your computer.

```bash
alias spike-starter-blueprint-cli-multicommands-python='spike-starter -t https://github.com/FabienArcellier/blueprint-cli-multicommands-python'
alias spike-starter-python3='spike-starter -t ~/projects/0004-spikes_template/python3_spike'
```

# Installation

1. install through pip

```bash
pip install spike-starter
```

After the installation, the command `spike_starter` can be used
from anywhere on your system.

2. install from the source

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

# Alternative

This tool is a pet project. I encourage you to take a look on other alternative.

* [Cookiecutter](https://cookiecutter.readthedocs.io/) is a more mature alternative to build project from project template. There is
  a [huge ecosystem of templates](https://cookiecutter.readthedocs.io/en/1.7.0/README.html#a-pantry-full-of-cookiecutters) available on internet

# License

```
MIT License
-----------

Copyright (c) 2019 Fabien Arcellier
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```
