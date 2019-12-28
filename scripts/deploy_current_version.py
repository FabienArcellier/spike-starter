#!/usr/bin/env python

import logging
import os
import sys

import pkg_resources
from git import Repo

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..', '..'))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('tag')


def main(arguments):
  os.chdir(ROOT_DIR)

  package_info = pkg_resources.require('spike_starter')[0]  # type:pkg_resources.EggInfoDistribution
  package_version = package_info.version
  target_tag = 'v{}'.format(package_version)

  repo = Repo(ROOT_DIR)
  if target_tag in repo.tags:
    raise OSError('the version {} has already been deployed'.format(target_tag))

  _system('git tag -a {} -m ""'.format(target_tag))
  _system('git push {}'.format(target_tag))


# BOILERPLATE TO REPRODUCE -ex behavior of bash

def _system(cmd, logged=True):
  if logged:
    print('$ {0}'.format(cmd))

  output = os.system(cmd)

  # see : https://stackoverflow.com/a/6466753
  error_code = output >> 8
  if error_code > 0:
    raise OSError(error_code)


if __name__ == '__main__':
  try:
    main(sys.argv[1:])
  except (OSError) as e:
    logger.critical(e)
    sys.exit(e.args[0])
