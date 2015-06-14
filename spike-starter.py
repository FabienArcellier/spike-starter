#!/usr/bin/python

import sys, traceback
import os
import git
from datetime import datetime

def main():
    try:
        # Read project name from command line
        project_name = sys.argv[1]

        spikeStarter = SpikeStarter()

        # Create project directory
        project_directory_name = spikeStarter.getProjectPath(project_name)
        project_directory = os.path.abspath(project_directory_name)
        spikeStarter.createProjectDirectory(project_directory)

        # Initialize git repository
        spikeStarter.createGitLocalRepository(project_directory)

    except SystemExit:
        sys.exit(1)

    except:
        print "Unexpected error:"
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

class SpikeStarter:

    def __init__(self):
        pass

    def getProjectPath(self, projectName):
        # project id from today date
        now = datetime.now()
        project_id = "{0:d}{1:0>2d}{2:0>2d}_{3:0>2d}{4:0>2d}".format(now.year, now.month, now.day, now.hour, now.minute)
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

def logAlert(text):
    print "[ALERT] {}".format(text)

def logInformation(text):
    print "[INFO] ", text

def logDebug(text):
    print "[DEBUG] ", text

if __name__ == "__main__":
    main()
