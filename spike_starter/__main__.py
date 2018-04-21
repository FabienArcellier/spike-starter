#!/usr/bin/python

import getopt
import logging
import os
import shutil
import sys
from datetime import datetime

import git


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
  print "python %s (-h) [-t template_path] projects" % (sys.argv[0])


class SpikeStarter(object):

  def __init__(self):
    pass

  def get_project_path(self, project_name):
    # project id from today date
    now = datetime.now()
    project_id = "{0:d}{1:0>2d}{2:0>2d}_{3:0>2d}{4:0>2d}".format(
      now.year, now.month, now.day, now.hour, now.minute)
    log_debug("project_id: {}".format(project_id))
    return "{}__{}".format(project_id, project_name)

  def create_project_directory(self, path):
    if not os.path.exists(path):
      os.makedirs(path)
      log_information("PROJECT DIRECTORY : {} [OK]".format(path))
    else:
      log_alert("Project already exits %s" % path)
      sys.exit(1)

  def create_git_local_repository(self, path):
    git.Repo.init(path)
    log_information("PROJECT GIT REPOSITORY : {} [OK]".format(path))

  def import_template_directory(self, destination, source):
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns('.git'))


def log_alert(text):
  print "[ALERT] {}".format(text)


def log_information(text):
  print "[INFO] ", text


def log_debug(text):
  print "[DEBUG] ", text


if __name__ == "__main__":
  main(sys.argv[1:])
