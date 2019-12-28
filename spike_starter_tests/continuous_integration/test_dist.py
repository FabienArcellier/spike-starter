import io
import os
import unittest

import pkg_resources

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..', '..'))
DIST_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'dist'))
EGG_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'spike_starter.egg-info'))


class TestDist(unittest.TestCase):

  def test_dist_generate_generate_dist_directory_with_archive_distributions(self):
    # Assign
    pkg_info = pkg_resources.require('spike-starter')[0]  # type:pkg_resources.EggInfoDistribution
    package_name = pkg_resources.to_filename(pkg_info.project_name)
    package_version = pkg_info.version
    package_fullname = "{}-{}".format(package_name, package_version)
    source_distribution = os.path.join(DIST_DIR, '{}.tar.gz'.format(package_fullname))
    binary_distribution = os.path.join(DIST_DIR, '{}-py3-none-any.whl'.format(package_fullname))

    # Assert
    self.assertTrue(os.path.isdir(DIST_DIR), '{0} does not exists'.format(DIST_DIR))
    dist_dir_contents = os.listdir(DIST_DIR)

    self.assertEqual(2, len(dist_dir_contents),
                     "dist directory contains more than 2 distribution archives : {0}".format(dist_dir_contents))

    self.assertTrue(os.path.isfile(source_distribution),
                    "source distribution {} does not exists".format(source_distribution))

    self.assertTrue(os.path.isfile(binary_distribution),
                    "binary distribution {} does not exists".format(binary_distribution))

  def test_long_description_should_be_markdown(self):
    """
    A deployment on pypi raise this error

    NOTE: Try --verbose to see response content.
    HTTPError: 400 Client Error: The description failed to render
    in the default format of reStructuredText. See https://pypi.org/help/#description-content-type
    for more information. for url: https://upload.pypi.org/legacy/
    """
    pkg_info_file = os.path.join(EGG_DIR, 'PKG-INFO')
    with io.open(pkg_info_file) as f:
      pkg_info = f.read()

    mandatory_header = 'Description-Content-Type:'
    header_content = 'Description-Content-Type: text/markdown'

    self.assertTrue(mandatory_header in pkg_info,
                    '{} is missing in {}'.format(mandatory_header, pkg_info_file))

    self.assertTrue(header_content in pkg_info,
                    '{} is not text/markdown in {}'.format(mandatory_header, pkg_info_file))

  def test_automatics_tests_and_scripts_are_not_in_archive_distributions(self):
    sources_file = os.path.join(EGG_DIR, 'SOURCES.txt')

    with io.open(sources_file) as f:
      sources = f.readlines()

    unallow_sources = ['spike_starter_tests', 'scripts']
    invalid_sources = []
    for source in sources:
      for unallow_source in unallow_sources:
        if source.startswith(unallow_source):
          invalid_sources.append(source)

    self.assertEqual(0, len(invalid_sources), "invalid source in {} : {}".format(sources_file, invalid_sources))


