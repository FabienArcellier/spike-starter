import logging
import os
import shutil
import tempfile

from datetime import datetime

import git


class SpikeStarter:

  def __init__(self):
    self.logger = logging.getLogger('spike-starter')

  def get_project_path(self, project_name):
    # project id from today date
    now = datetime.now()
    project_id = "{0:d}{1:0>2d}{2:0>2d}_{3:0>2d}{4:0>2d}".format(
      now.year, now.month, now.day, now.hour, now.minute)
    self.logger.debug("project_id:%s", project_id)
    return "{}__{}".format(project_id, project_name)

  def create_project_directory(self, path):
    if not os.path.exists(path):
      os.makedirs(path)
      self.logger.info("The spike project is ready.")
      self.logger.info("DIRECTORY :%s [OK]", path)
    else:
      self.logger.info("Project already exits %s", path)
      raise OSError()

  def create_git_local_repository(self, path):
    git.Repo.init(path)
    self.logger.info("The spike project is ready.")
    self.logger.info("DIRECTORY :%s [OK]", path)

  def import_template_directory(self, destination: str, source: str) -> None:
    blueprint_origin = self._blueprint_origin(source)

    self.logger.debug('import_template_directory - blueprint_origin:%s source:%s destination:%s'
                      , blueprint_origin, source, destination)

    if blueprint_origin == 'local':
      shutil.copytree(source, destination, ignore=shutil.ignore_patterns('.git'))

    if blueprint_origin == 'git':
      clone_destination = tempfile.mktemp(prefix='spike_starter_')
      git.Repo.clone_from(source, clone_destination, multi_options=['--depth=1'])
      shutil.copytree(clone_destination, destination, ignore=shutil.ignore_patterns('.git'))
      shutil.rmtree(clone_destination)

    self.logger.debug('import_template_directory - done')

  def _blueprint_origin(self, source: str) -> [str]:
    blueprint_origin = None
    if source.endswith('.git') and source.startswith('https://'):
      blueprint_origin = 'git'

    if source.endswith('.git') and source.startswith('git@'):
      blueprint_origin = 'git'

    if os.path.exists(source):
      blueprint_origin = 'local'

    return blueprint_origin
