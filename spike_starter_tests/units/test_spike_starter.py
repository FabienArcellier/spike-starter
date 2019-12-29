import unittest
from unittest import mock

from spike_starter.__main__ import SpikeStarter


class TestSpikeStarter(unittest.TestCase):

  def setUp(self) -> None:
    self._tested = SpikeStarter()


  def test_blueprint_origin_is_git_when_it_s_end_with_dot_git_and_support_https(self):
    # Acts
    blueprint_origin = self._tested._blueprint_origin('https://github.com/FabienArcellier/spike-starter.git')

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
