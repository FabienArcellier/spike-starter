import os
import tempfile

import shutil

SCRIPT_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIRECTORY_PATH = os.path.join(SCRIPT_DIRECTORY_PATH, 'templates')

def clone_template(template_name, working_dir=None):
  working_directory = tempfile.mktemp(prefix='fixtures_') if not working_dir else working_dir
  template_working_directory = os.path.join(TEMPLATE_DIRECTORY_PATH, template_name)

  if not os.path.isdir(template_working_directory):
    fixtures_content = [d for d in os.listdir(SCRIPT_DIRECTORY_PATH) if os.path.isdir(os.path.join(SCRIPT_DIRECTORY_PATH, d))]
    raise Exception('the template {0} does not exists in {1}'.format(template_name, fixtures_content))

  shutil.copytree(template_working_directory, working_directory)
  return working_directory
