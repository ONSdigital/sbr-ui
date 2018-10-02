import unittest
import os

from sbr_ui.models.exceptions import InvalidEnvironment, MissingEnvironmentVariable
from sbr_ui.utilities.server_startup import get_and_validate_environment, check_required_environment_variables_present


class TestConfig(unittest.TestCase):

    def tearDown(self):
        """ Reset the ENVIRONMENT so the subsequent tests don't fail """
        os.environ['ENVIRONMENT'] = 'TEST'

    def test_app_fails_on_invalid_environment(self):
        os.environ['ENVIRONMENT'] = 'AAA'
        with self.assertRaises(InvalidEnvironment):
            get_and_validate_environment()

    def test_app_fails_if_env_vars_missing(self):
        os.environ['ENVIRONMENT'] = 'PROD'
        config = {"REQUIRED_VARS": ["ENVIRONMENT", "API_URL"]}
        with self.assertRaises(MissingEnvironmentVariable):
            check_required_environment_variables_present('PROD', config)
