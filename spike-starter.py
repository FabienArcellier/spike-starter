#!/usr/bin/python

import sys
import os
import git

def main():
    try:
        # lire le nom du projet
        project_id = sys.argv[1]
        project_name = sys.argv[2]

        # creer un dossier
        project_directory = os.path.abspath("%s_%s" % (project_id, project_name))
        logDebug("project_directory: %s" % project_directory)

        if not os.path.exists(project_directory):
            os.makedirs(project_directory)
            logInformation("PROJECT DIRECTORY : %s [OK]" % project_directory)
        else:
            logAlert("Project already exits %s" % project_directory)
            sys.exit(1)

        # Creer un depot git
        project_repository = git.Repo.init(project_directory)
        logInformation("PROJECT GIT REPOSITORY : %s [OK]" % project_directory)

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
