#!/usr/bin/python

import getopt
import logging
import os
import sys


from spike_starter.spike_starter import SpikeStarter


def cli():
  main(sys.argv[1:])


def main(argv):
  # pylint: disable=broad-except
  try:
    # Read project name from command line
    template_dir = ""
    template = False
    opts, args = getopt.getopt(argv, "ht:", ["help", "template="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        usage()
        sys.exit()
      elif opt in ("-t", "--template"):
        template = True
        template_dir = arg

    spike_starter = SpikeStarter()
    for project_name in args:

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


def usage():
  print("python %s (-h) [-t template_path] projects" % (sys.argv[0]))


if __name__ == "__main__":
  main(sys.argv[1:])
