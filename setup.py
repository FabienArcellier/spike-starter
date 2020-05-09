#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name='spike_starter',
  version='0.1.7',
  description="spike-starter creates project from blueprint template",
  packages=find_packages(exclude=["spike_starter_tests", "spike_starter_tests.*"]),
  license='MIT',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  classifiers=[
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License'
  ],
  entry_points={
    'console_scripts': [
      'spike-starter = spike_starter.__main__:main',
    ],
  },
  install_requires=[
    'click',
    'decorator',
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
