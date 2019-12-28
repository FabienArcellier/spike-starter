#!/usr/bin/env python
import os
import shutil
import tempfile
import unittest

from spike_starter.__main__ import SpikeStarter
from spike_starter_tests.fixtures import clone_template


class TestSpikeStarter(unittest.TestCase):
  def setUp(self):
    self._tested = SpikeStarter()

  def test_importTemplateDirectory_should_copy_the_source_directory_into_destination(self):
    source = clone_template('template_project')
    destination = tempfile.mktemp(prefix='fixtures_')

    try:
      # Acts
      self._tested.import_template_directory(destination, source)

      # Assert
      expected_path = os.path.join(destination, 'file.txt')
      self.assertEqual(True, os.path.exists(expected_path), '{0} should a clone'.format(expected_path))
    finally:
      if os.path.isdir(source) : shutil.rmtree(source)
      if os.path.isdir(destination) : shutil.rmtree(destination)

  def test_importTemplateDirectory_should_not_copy_git_subdirectory_from_the_source(self):
    source = clone_template('template_project')
    destination = tempfile.mktemp(prefix='fixtures_')
    os.makedirs(os.path.join(source, '.git'))
    os.makedirs(os.path.join(source, 'subidr1/.git'))

    try:
      # Acts
      self._tested.import_template_directory(destination, source)

      # Assert
      expected_path = os.path.join(destination, '.git')
      self.assertEqual(False, os.path.exists(expected_path), '{0} should not be cloned'.format(expected_path))

      expected_path = os.path.join(destination, 'subdir1/.git')
      self.assertEqual(False, os.path.exists(expected_path), '{0} should not be cloned'.format(expected_path))
    finally:
      if os.path.isdir(source) : shutil.rmtree(source)
      if os.path.isdir(destination) : shutil.rmtree(destination)
