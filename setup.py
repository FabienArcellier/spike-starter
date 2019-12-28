#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name='spike_starter',
  version='0.0.7',
  packages=find_packages(exclude=["spike_starter_tests", "spike_starter_tests.*"]),
  license='',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
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
      'tox',
      'twine'
    ]
  }
)
