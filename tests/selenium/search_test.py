import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from tests.helper_methods import create_selenium_config

from tests.constants import BASE_URL, ERROR_URL, SEARCH_URL, RURN, UNIT_TYPE_INPUT_ID, PERIOD_INPUT_ID
from tests.constants import SBR_DESCRIPTION_ID, SEARCH_BUTTON_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, SEARCH_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ENTREF, UBRN, LURN, VATREF, PAYEREF, CRN, PERIOD
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD


class SearchTest(unittest.TestCase):
    """
        These tests ensure that searching from the home page works, another test class will handle the testing
        of each unit page and navigating between units using the breadcrumb and list of child units.
    """

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

    def input_unit_id_type_period_and_search(self, unit_id, unit_type, period):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(unit_id)
        self.driver.find_element_by_id(UNIT_TYPE_INPUT_ID).send_keys(unit_type)
        self.driver.find_element_by_id(PERIOD_INPUT_ID).send_keys(period)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()

    def test_search_input_focus(self):
        """ Ensure the search input has focus """
        search_input = self.driver.find_element_by_id(SEARCH_INPUT_ID)
        self.assertEqual(search_input, self.driver.switch_to.active_element)

    def test_header_text(self):
        """ Ensure the SBR description text that is present on login/home pages is no longer present. """
        self.input_unit_id_type_period_and_search(ENTREF, 'ENT', '201810')
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_id(SBR_DESCRIPTION_ID)

    def test_search_ent(self):
        self.input_unit_id_type_period_and_search(ENTREF, 'ENT', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/ENT/units/{ENTREF}')

    def test_search_lou(self):
        self.input_unit_id_type_period_and_search(LURN, 'LOU', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/LOU/units/{LURN}')

    def test_search_reu(self):
        self.input_unit_id_type_period_and_search(RURN, 'REU', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/REU/units/{RURN}')

    def test_search_leu(self):
        self.input_unit_id_type_period_and_search(UBRN, 'LEU', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/LEU/units/{UBRN}')

    def test_search_ch(self):
        self.input_unit_id_type_period_and_search(CRN, 'CH', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/CH/units/{CRN}')

    def test_search_vat(self):
        self.input_unit_id_type_period_and_search(VATREF, 'VAT', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/VAT/units/{VATREF}')

    def test_search_paye(self):
        self.input_unit_id_type_period_and_search(PAYEREF, 'PAYE', '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/PAYE/units/{PAYEREF}')

    def test_unit_not_found(self):
        self.input_unit_id_type_period_and_search('Tesco', 'ENT', '201810')
        self.assertEqual(self.driver.current_url, ERROR_URL)
        self.assertTrue('404 - Not Found' in self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
