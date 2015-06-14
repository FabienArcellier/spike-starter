#!/usr/bin/python

import sys
import traceback
import os
import getopt
import git
from datetime import datetime


def main(argv):
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

    spikeStarter = SpikeStarter()
    for project_name in args:

      # Create project directory
      project_directory_name = spikeStarter.getProjectPath(project_name)
      project_directory = os.path.abspath(project_directory_name)
      spikeStarter.createProjectDirectory(project_directory)

      # Initialize git repository
      spikeStarter.createGitLocalRepository(project_directory)

      if template:
        spikeStarter.importTemplateDirectory(project_directory, template_dir)

  except SystemExit:
    sys.exit(1)

  except:
    print "Unexpected error:"
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)


def usage():
  print "python %s (-h) [-t template_path] projects" % (sys.argv[0])


class SpikeStarter:

  def __init__(self):
    pass

  def getProjectPath(self, projectName):
    # project id from today date
    now = datetime.now()
    project_id = "{0:d}{1:0>2d}{2:0>2d}_{3:0>2d}{4:0>2d}".format(
        now.year, now.month, now.day, now.hour, now.minute)
    logDebug("project_id: {}".format(project_id))
    return "{}__{}".format(project_id, projectName)

  def createProjectDirectory(self, path):
    if not os.path.exists(path):
      os.makedirs(path)
      logInformation("PROJECT DIRECTORY : {} [OK]".format(path))
    else:
      logAlert("Project already exits %s" % path)
      sys.exit(1)

  def createGitLocalRepository(self, path):
    project_repository = git.Repo.init(path)
    logInformation("PROJECT GIT REPOSITORY : {} [OK]".format(path))

  def importTemplateDirectory(self, destination, source):
    pass


def logAlert(text):
  print "[ALERT] {}".format(text)


def logInformation(text):
  print "[INFO] ", text


def logDebug(text):
  print "[DEBUG] ", text

if __name__ == "__main__":
  main(sys.argv[1:])
