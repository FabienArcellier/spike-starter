import os
import unittest
from unittest import mock
from unittest.mock import patch

from spike_starter.__main__ import SpikeStarter


class TestSpikeStarter(unittest.TestCase):

  def setUp(self) -> None:
    self._tested = SpikeStarter(noprefix=False)


  def test_blueprint_origin_is_git_when_it_s_end_with_dot_git_and_support_https(self):
    # Acts
    blueprint_origin = self._tested._blueprint_origin('https://github.com/FabienArcellier/spike-starter.git')

    # Assert
    self.assertEqual('git', blueprint_origin)

  def test_blueprint_origin_is_git_when_it_s_end_with_dot_git_and_support_ssh(self):
    # Acts
    blueprint_origin = self._tested._blueprint_origin('git@github.com:FabienArcellier/spike-starter.git')

    # Assert
    self.assertEqual('git', blueprint_origin)

  def test_blueprint_origin_is_local_when_it_exists_on_local_disk(self):
    with mock.patch('os.path.exists', return_value = True):
      # Acts
      blueprint_origin = self._tested._blueprint_origin('/tmp')

      # Assert
      self.assertEqual('local', blueprint_origin)

  def test_blueprint_origin_is_none_when_it_match_no_other_option(self):
    with mock.patch('os.path.exists', return_value = False):
      # Acts
      blueprint_origin = self._tested._blueprint_origin('/tmp')

      # Assert
      self.assertEqual(None, blueprint_origin)

  def test_get_project_path_does_append_date_by_default(self):
    # Assign

    # Acts
    project_path = self._tested.get_project_path('myproject')

    # Assert
    project_directory = os.path.basename(project_path)
    self.assertTrue(project_directory.endswith('_myproject'), f'wrong project directory {project_directory}')
    
  
  def test_get_project_path_does_not_append_date_when_no_prefix(self):
    # Assign
    tested = SpikeStarter(noprefix=True)

    # Acts
    project_path = tested.get_project_path('myproject')

    # Assert
    project_directory = os.path.basename(project_path)
    self.assertEqual('myproject', project_directory)
  
  def test_is_in_git_repository_should_detect_if_the_spike_is_in_git_repository(self):
    with patch('os.path.isdir', side_effect=_side_effect_in_git_repository) as m:
      # Assign
      path = '/bla/bla/bla/bla/my_repository'

      # Acts
      is_in_git_repository = self._tested.is_in_git_repository(path)

      # Assert
      self.assertTrue(is_in_git_repository)


def _side_effect_in_git_repository(*args):
  if args[0] == '/bla/.git':
    return True
  else:
    return False
