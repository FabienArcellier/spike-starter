#!/usr/bin/python

import sys
import os
import git
from datetime import datetime

def main():
    try:
        # Read project name from command line
        project_name = sys.argv[1]

        # project id from today date
        now = datetime.now()
        project_id = "{0:d}{1:0>2d}{2:0>2d}_{3:0>2d}{4:0>2d}".format(now.year, now.month, now.day, now.hour, now.minute)
        logDebug("project_id: {}".format(project_id))


        # Create project directory
        project_directory = os.path.abspath("{}__{}".format(project_id, project_name))
        logDebug("project_directory: {}".format(project_directory))

        if not os.path.exists(project_directory):
            os.makedirs(project_directory)
            logInformation("PROJECT DIRECTORY : {} [OK]".format(project_directory))
        else:
            logAlert("Project already exits %s" % project_directory)
            sys.exit(1)

        # Initialize git repository
        project_repository = git.Repo.init(project_directory)
        logInformation("PROJECT GIT REPOSITORY : {} [OK]".format(project_directory))

        # Creer un fichier .gitignore


    except SystemExit:
        sys.exit(1)

    except:
        print "Unexpected error:", sys.exc_info()
        sys.exit(1)

def logAlert(text):
    print "[ALERT] %s" % text

def logInformation(text):
    print "[INFO] ", text

def logDebug(text):
    print "[DEBUG] ", text

if __name__ == "__main__":
    main()
