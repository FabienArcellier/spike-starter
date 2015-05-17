#!/usr/bin/python

import sys
import os

def logInformation(text):
    print "[INFO] ", text

if __name__ == "__main__":
    # lire le nom du projet
    project_id = sys.argv[1]
    project_name = sys.argv[2]

    project_directory = os.path.abspath("%s_%s" % (project_id, project_name))

    # creer un dossier
    if not os.path.exists(project_directory):
        os.makedirs(project_directory)
        logInformation("CREATE PROJECT DIR %s" % project_directory)
