import unittest
from selenium import webdriver

from tests.helper_methods import flatten, create_selenium_config
from test_data import enterprise, legal_unit

from tests.constants import BASE_URL, SEARCH_URL, UNIT_TYPE_INPUT_ID, PERIOD_INPUT_ID, BREADCRUMB_ENT_ID
from tests.constants import SEARCH_BUTTON_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, SEARCH_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ENTREF, UBRN, PERIOD
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD


class UnitPageNavigationTest(unittest.TestCase):

    def setUp(self):
        self.options = create_selenium_config()
        self.driver = webdriver.Firefox(firefox_options=self.options)
        self.driver.get(BASE_URL)
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(ADMIN_USERNAME)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(ADMIN_PASSWORD)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()

    def tearDown(self):
        self.driver.find_element_by_id(LOGOUT_BUTTON_ID).click()
        self.driver.quit()

    def search_by_unit_id_type_period(self, unit_id, unit_type, period):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(unit_id)
        self.driver.find_element_by_id(UNIT_TYPE_INPUT_ID).send_keys(unit_type)
        self.driver.find_element_by_id(PERIOD_INPUT_ID).send_keys(period)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()

    def assert_title(self, title_id, expected_title):
        title = self.driver.find_element_by_id(title_id).text
        self.assertEqual(title, expected_title)

    def assert_dict_values_present_on_page(self, unit_vars):
        """
        Assert that every value in a dictionary is present on the page
        Flattening the dict structure makes things easier than checking for nested dicts
        """
        flattened_vars = flatten(unit_vars)
        for unit_variable in list(flattened_vars.values()):
            self.assertTrue(unit_variable in self.driver.page_source)

    def test_browser_back_button_leu_to_ent(self):
        """ To ensure there aren't caching issues, we need to test the browser back button. """
        self.search_by_unit_id_type_period(UBRN, 'LEU', PERIOD)
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/LEU/units/{UBRN}')
        self.assert_dict_values_present_on_page(legal_unit.get('vars'))
        self.driver.find_element_by_id(BREADCRUMB_ENT_ID).click()
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/ENT/units/{ENTREF}')
        self.assert_dict_values_present_on_page(enterprise.get('vars'))
        self.driver.back()
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/LEU/units/{UBRN}')
        self.assert_dict_values_present_on_page(legal_unit.get('vars'))


if __name__ == '__main__':
    unittest.main()
