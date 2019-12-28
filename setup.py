#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name='spike_starter',
  version='0.0.7',
  packages=find_packages(exclude=["*_tests"]),
  license='',
  long_description=open('README.md').read(),
  classifiers=[
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python :: 3'
  ],
  entry_points={
    'console_scripts': [
      'spike-starter = spike_starter.__main__:cli',
    ],
  },
  install_requires=[
    'click',
    'GitPython'
  ],
  extras_require={
    'dev': [
      'pylint',
      'tox'
    ]
  }
)
