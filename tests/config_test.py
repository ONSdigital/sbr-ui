import unittest
import os

from sbr_ui import validate_environment, InvalidEnvironment


class TestConfig(unittest.TestCase):

    def test_app_fails_on_invalid_environment(self):
        os.environ['ENVIRONMENT'] = 'AAA'
        with self.assertRaises(InvalidEnvironment):
            validate_environment()

    # TODO: fix below test, need to sort out circular dependancies in the main __init__.py file
    # def test_app_fails_if_env_vars_missing(self):
    #     os.environ['ENVIRONMENT'] = 'PROD'
    #     with self.assertRaises(MissingEnvironmentVariable):
    #         check_required_env_vars('PROD', app.config)
