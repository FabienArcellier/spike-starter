#!/usr/bin/python

import logging
import os
import sys

import click
import pkg_resources
from click import Command

from spike_starter.spike_starter import SpikeStarter


@click.command('spike-starter', help='create a project from a project blueprint')
@click.option('--template', '-t', default=None, help='template path either local or git path')
@click.option('--debug', '-d', is_flag=True, help='show debug information')
@click.option('--version', '-v', is_flag=True, help='show version number')
@click.option('--noprefix', is_flag=True, help='remove prefix with date and time')
@click.argument('project_names', nargs=-1)
def main(template: str, debug: bool, version: bool, noprefix: bool, project_names: [str]):
  # pylint: disable=broad-except
  configure_logging(debug)

  if version:
    # pylint: disable=line-too-long
    package_info = pkg_resources.require('spike_starter')[0]  # type:pkg_resources.EggInfoDistribution
    package_version = package_info.version
    print(package_version)
    sys.exit(0)

  if len(project_names) == 0:
    print_help_msg(main)
    sys.exit(2)

  try:
    template_dir = template

    # pylint: disable=simplifiable-if-expression
    has_template = False if not template_dir else True

    spike_starter = SpikeStarter(noprefix)
    for project_name in project_names:

      project_directory_name = spike_starter.get_project_path(project_name)
      project_directory = os.path.abspath(project_directory_name)

      if has_template:
        spike_starter.import_template_directory(project_directory, template_dir)
      else:
        spike_starter.create_project_directory(project_directory)

      spike_starter.create_git_local_repository(project_directory)

  except SystemExit:
    sys.exit(1)

  except Exception:
    logging.exception("Unexpected error:")
    sys.exit(1)


def configure_logging(debug):
  if debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)

def print_help_msg(command: Command):
  with click.Context(command, info_name=command.name) as ctx:
    click.echo(command.get_help(ctx))

if __name__ == '__main__':
  # pylint: disable=no-value-for-parameter
  main()
