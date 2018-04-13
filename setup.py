#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name='spike_starter',
  version='0.0.4',
  packages=find_packages(exclude=["*_tests"]),
  license='',
  long_description=open('README.md').read(),
  entry_points={
    'console_scripts': [
      'spike-starter = spike_starter.__main__:cli',
    ],
  },
  install_requires=[
    'click',
    'GitPython'
  ]
)
