#!/usr/bin/env python

import logging
import os
import sys
from importlib.metadata import version

from git import Repo

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('tag')


def main(arguments):
  os.chdir(ROOT_DIR)

  target_tag = 'v{}'.format(version('spike-starter'))

  repo = Repo(ROOT_DIR)
  if target_tag in repo.tags:
    raise OSError(f'the version {target_tag} has already been deployed')

  _system(f'git tag -a {target_tag} -m ""')
  _system(f'git push origin {target_tag}')


# BOILERPLATE TO REPRODUCE -ex behavior of bash

def _system(cmd, logged=True):
  if logged:
    print(f'$ {cmd}')

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
