import unittest

from click.testing import CliRunner
from spike_starter.__main__ import main


class Test__main__(unittest.TestCase):

  def test_main_should_show_usage_when_there_is_no_arguments_in_cli(self):
    # Assign
    runner = CliRunner()

    # Acts
    result = runner.invoke(main, [])

    # Assert
    self.assertEqual(result.exit_code, 2)
    self.assertTrue('Usage: spike-starter' in result.output,'{} not in {}'.format('Usage: spike-starter', result.output))
