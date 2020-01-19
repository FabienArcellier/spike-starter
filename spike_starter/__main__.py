#!/usr/bin/python

import logging
import os
import sys

import click

from spike_starter.spike_starter import SpikeStarter

logging.basicConfig(level=logging.INFO)


@click.command('spike-starter', help='create a project from a project blueprint')
@click.option('--template', '-t', help='template path either local or git path')
@click.argument('project_names', nargs=-1, required=True)
def main(template, project_names):
  # pylint: disable=broad-except
  try:
    # Read project name from command line
    template_dir = ""
    template = False

    spike_starter = SpikeStarter()
    for project_name in project_names:

      # Create project directory
      project_directory_name = spike_starter.get_project_path(project_name)
      project_directory = os.path.abspath(project_directory_name)

      if template:
        spike_starter.import_template_directory(project_directory, template_dir)
      else:
        spike_starter.create_project_directory(project_directory)

      # Initialize git repository
      spike_starter.create_git_local_repository(project_directory)

  except SystemExit:
    sys.exit(1)

  except Exception:
    logging.exception("Unexpected error:")
    sys.exit(1)


if __name__ == '__main__':
  # pylint: disable=no-value-for-parameter
  main()
