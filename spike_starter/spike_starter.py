import logging
import os
import shutil
import tempfile

from datetime import datetime

import git


class SpikeStarter:

  def __init__(self, noprefix: bool):
    self.logger = logging.getLogger('spike-starter')
    self.logger.debug('test')
    self._no_prefix = noprefix

  def get_project_path(self, project_name: str)->str:
    project_path = None
    if self._no_prefix:
      project_path = os.path.abspath(project_name)
    else:
      now = datetime.now()
      project_id = f"{now.year:d}{now.month:0>2d}{now.day:0>2d}_{now.hour:0>2d}{now.minute:0>2d}"
      project_path = os.path.abspath(f"{project_id}__{project_name}")
    self.logger.debug("project_path:%s", project_path)
    return project_path

  def create_project_directory(self, path):
    if not os.path.exists(path):
      os.makedirs(path)
      self.logger.debug({"operation": "create_project_directory", "path": path, "status": "OK"})
    else:
      self.logger.info("Project already exits %s", path)
      raise OSError()

  def is_in_git_repository(self, path: str) -> bool:
    is_in_git = False
    head, tail = os.path.split(path)
    while tail != '':
      if os.path.isdir(os.path.join(head, '.git')):
        is_in_git = True
        break

      head, tail = os.path.split(head)

    return is_in_git

  def create_git_local_repository(self, path):
    git.Repo.init(path)
    self.logger.info("The spike project is ready.")
    self.logger.info("DIRECTORY :%s [OK]", path)

  def import_template_directory(self, destination: str, source: str) -> None:
    blueprint_origin = self._blueprint_origin(source)

    self.logger.debug({
      "operation": "import_template_directory",
      "blueprint_origin": blueprint_origin,
      "source": source,
      "destination": destination
    })

    if blueprint_origin == 'local':
      shutil.copytree(source, destination, ignore=shutil.ignore_patterns('.git'))

    if blueprint_origin == 'git':
      clone_destination = tempfile.mktemp(prefix='spike_starter_')
      git.Repo.clone_from(source, clone_destination, multi_options=['--depth=1'])
      shutil.copytree(clone_destination, destination, ignore=shutil.ignore_patterns('.git'))
      shutil.rmtree(clone_destination)

    self.logger.debug({"operation": "import_template_directory", "status": "OK"})

  def _blueprint_origin(self, source: str) -> [str]:
    blueprint_origin = None
    if source.endswith('.git') and source.startswith('https://'):
      blueprint_origin = 'git'

    if source.endswith('.git') and source.startswith('git@'):
      blueprint_origin = 'git'

    if os.path.exists(source):
      blueprint_origin = 'local'

    return blueprint_origin
