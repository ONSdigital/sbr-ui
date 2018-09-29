import unittest
from selenium import webdriver

from tests.helper_methods import flatten, create_selenium_config
from test_data import enterprise, legal_unit, local_unit, company_house, value_added_tax, pay_as_you_earn

from tests.constants import BASE_URL
from tests.constants import SEARCH_BUTTON_ID, UNIT_NAME_ID, UNIT_BADGE_ID, UNIT_ID_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, SEARCH_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ENTREF, UBRN, LURN, VATREF, PAYEREF, CRN, PERIOD
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD


class UnitPageTest(unittest.TestCase):
    """
        UnitPageTest asserts that all the variables within the test data are present on the page.
        The name and id are tested normally using the id in the html, for the other variables, there
        is an assertion to see if the value is present anywhere on the page, which could be improved upon.
        e.g. if a variable value is missing on the unit data part of the page but present in a text input or
        somewhere else on the page, it would pass. This is probably fine for now.
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

    def search_by_unit_id(self, unit_id):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(unit_id)
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

    def test_ent_page_contents(self):
        self.search_by_unit_id(ENTREF)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/ENT/units/{ENTREF}')
        self.assert_title(UNIT_NAME_ID, enterprise.get('vars').get('name'))
        self.assertEqual(self.driver.find_element_by_id(UNIT_BADGE_ID).text, 'ENTERPRISE')
        self.assertEqual(self.driver.find_element_by_id(UNIT_ID_ID).text, f'ERN {ENTREF}')
        self.assert_dict_values_present_on_page(enterprise.get('vars'))

    def test_leu_page_contents(self):
        self.search_by_unit_id(UBRN)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/LEU/units/{UBRN}')
        self.assert_title(UNIT_NAME_ID, legal_unit.get('vars').get('name'))
        self.assertEqual(self.driver.find_element_by_id(UNIT_BADGE_ID).text, 'LEGAL UNIT')
        self.assertEqual(self.driver.find_element_by_id(UNIT_ID_ID).text, f'UBRN {UBRN}')
        self.assert_dict_values_present_on_page(legal_unit.get('vars'))

    def test_lu_page_contents(self):
        self.search_by_unit_id(LURN)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/LU/units/{LURN}')
        self.assert_title(UNIT_NAME_ID, local_unit.get('vars').get('name'))
        self.assertEqual(self.driver.find_element_by_id(UNIT_BADGE_ID).text, 'LOCAL UNIT')
        self.assertEqual(self.driver.find_element_by_id(UNIT_ID_ID).text, f'LURN {LURN}')
        self.assert_dict_values_present_on_page(local_unit.get('vars'))

    def test_ch_page_contents(self):
        self.search_by_unit_id(CRN)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/CH/units/{CRN}')
        self.assert_title(UNIT_NAME_ID, company_house.get('vars').get('businessName'))
        self.assertEqual(self.driver.find_element_by_id(UNIT_BADGE_ID).text, 'COMPANY HOUSE')
        self.assertEqual(self.driver.find_element_by_id(UNIT_ID_ID).text, f'CRN {CRN}')
        self.assert_dict_values_present_on_page(company_house.get('vars'))

    def test_vat_page_contents(self):
        self.search_by_unit_id(VATREF)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/VAT/units/{VATREF}')
        self.assert_title(UNIT_NAME_ID, value_added_tax.get('vars').get('businessName'))
        self.assertEqual(self.driver.find_element_by_id(UNIT_BADGE_ID).text, 'VALUE ADDED TAX')
        self.assertEqual(self.driver.find_element_by_id(UNIT_ID_ID).text, f'VATREF {VATREF}')
        self.assert_dict_values_present_on_page(value_added_tax.get('vars'))

    def test_paye_page_contents(self):
        self.search_by_unit_id(PAYEREF)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/PAYE/units/{PAYEREF}')
        self.assert_title(UNIT_NAME_ID, pay_as_you_earn.get('vars').get('businessName'))
        self.assertEqual(self.driver.find_element_by_id(UNIT_BADGE_ID).text, 'PAY AS YOU EARN')
        self.assertEqual(self.driver.find_element_by_id(UNIT_ID_ID).text, f'PAYEREF {PAYEREF}')
        self.assert_dict_values_present_on_page(pay_as_you_earn.get('vars'))


if __name__ == '__main__':
    unittest.main()
