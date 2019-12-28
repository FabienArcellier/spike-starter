import os
import unittest

import pkg_resources

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
DIST_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..', '..', 'dist'))


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
