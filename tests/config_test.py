import unittest
import os

from sbr_ui import load_config, InvalidEnvironment, MissingEnvironmentVariable


class TestConfig(unittest.TestCase):

    def test_app_fails_on_invalid_environment(self):
        os.environ['ENVIRONMENT'] = 'AAA'
        with self.assertRaises(InvalidEnvironment):
            load_config()

    def test_app_fails_if_env_vars_missing(self):
        os.environ['ENVIRONMENT'] = 'PROD'
        with self.assertRaises(MissingEnvironmentVariable):
            load_config()
