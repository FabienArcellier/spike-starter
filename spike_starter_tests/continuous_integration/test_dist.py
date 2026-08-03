import os
import unittest
from importlib.metadata import version

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..', '..'))
DIST_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'dist'))
EGG_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'spike_starter.egg-info'))


class TestDist(unittest.TestCase):

  def test_dist_generate_generate_dist_directory_with_archive_distributions(self):
    # Assign
    package_name = 'spike-starter'.replace('-', '_')
    package_version = version('spike-starter')
    package_fullname = f"{package_name}-{package_version}"
    source_distribution = os.path.join(DIST_DIR, f'{package_fullname}.tar.gz')
    binary_distribution = os.path.join(DIST_DIR, f'{package_fullname}-py3-none-any.whl')

    # Assert
    self.assertTrue(os.path.isdir(DIST_DIR), f'{DIST_DIR} does not exists')
    dist_dir_contents = os.listdir(DIST_DIR)

    self.assertEqual(2, len(dist_dir_contents),
                     "dist directory contains more than 2 distribution archives : "
                     f"{dist_dir_contents}")

    self.assertTrue(os.path.isfile(source_distribution),
                    f"source distribution {source_distribution} does not exists")

    self.assertTrue(os.path.isfile(binary_distribution),
                    f"binary distribution {binary_distribution} does not exists")

  def test_long_description_should_be_markdown(self):
    """
    A deployment on pypi raise this error

    NOTE: Try --verbose to see response content.
    HTTPError: 400 Client Error: The description failed to render
    in the default format of reStructuredText. See https://pypi.org/help/#description-content-type
    for more information. for url: https://upload.pypi.org/legacy/
    """
    pkg_info_file = os.path.join(EGG_DIR, 'PKG-INFO')
    with open(pkg_info_file) as f:
      pkg_info = f.read()

    mandatory_header = 'Description-Content-Type:'
    header_content = 'Description-Content-Type: text/markdown'

    self.assertTrue(mandatory_header in pkg_info,
                    f'{mandatory_header} is missing in {pkg_info_file}')

    self.assertTrue(header_content in pkg_info,
                    f'{mandatory_header} is not text/markdown in {pkg_info_file}')

  def test_automatics_tests_and_scripts_are_not_in_archive_distributions(self):
    sources_file = os.path.join(EGG_DIR, 'SOURCES.txt')

    with open(sources_file) as f:
      sources = f.readlines()

    unallow_sources = ['spike_starter_tests', 'scripts']
    invalid_sources = []
    for source in sources:
      for unallow_source in unallow_sources:
        if source.startswith(unallow_source):
          invalid_sources.append(source)

    self.assertEqual(0, len(invalid_sources),
                     f"invalid source in {sources_file} : {invalid_sources}")


