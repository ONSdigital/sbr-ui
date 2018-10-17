import unittest
from selenium import webdriver

from tests.helper_methods import create_selenium_config

from tests.constants import BASE_URL, SEARCH_URL
from tests.constants import ENTERPRISE, LOCAL_UNIT, REPORTING_UNIT, LEGAL_UNIT, COMPANY_HOUSE, VALUE_ADDED_TAX, PAY_AS_YOU_EARN
from tests.constants import BREADCRUMB_SEARCH_ID, BREADCRUMB_SELECTED_ID, BREADCRUMB_ENT_ID, BREADCRUMB_LEU_ID
from tests.constants import SEARCH_BUTTON_ID, PERIOD_INPUT_ID, UNIT_TYPE_INPUT_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, SEARCH_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ERN, UBRN, RURN, LURN, VATREF, PAYEREF, CRN, PERIOD
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD


class BreadcrumbTest(unittest.TestCase):
    """
        The breadcrumb is present on each unit page and allows navigation up the unit hierarchy.
        TODO: test for when a breadcrumb link returns 404/500
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

    def search_by_unit_id_type_period(self, unit_id, unit_type, period):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(unit_id)
        self.driver.find_element_by_id(UNIT_TYPE_INPUT_ID).send_keys(unit_type)
        self.driver.find_element_by_id(PERIOD_INPUT_ID).send_keys(period)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()

    def assert_breadcrumb_item_text_and_url(self, breadcrumb_id, unit_id, unit_type, period):
        breadcrumb_item = self.driver.find_element_by_id(breadcrumb_id)
        self.assertEqual(breadcrumb_item.text, f'{unit_type} - {unit_id}')
        target_url = f'{SEARCH_URL}/periods/{period}/types/{unit_type}/units/{unit_id}'
        self.assertEqual(breadcrumb_item.get_attribute('href'), target_url)

    def assert_current_breadcrumb_item_text(self, expected_text):
        current_item_text = self.driver.find_element_by_id(BREADCRUMB_SELECTED_ID).text
        self.assertEqual(current_item_text, expected_text)

    def assert_breadcrumb_search_href(self):
        href = self.driver.find_element_by_id(BREADCRUMB_SEARCH_ID).get_attribute('href')
        self.assertEqual(href, SEARCH_URL)

    def test_ent_breadcrumb(self):
        self.search_by_unit_id_type_period(ERN, ENTERPRISE, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{ENTERPRISE}/units/{ERN}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'ENT - {ERN}')

    def test_lou_breadcrumb(self):
        self.search_by_unit_id_type_period(LURN, LOCAL_UNIT, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{LOCAL_UNIT}/units/{LURN}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'LOU - {LURN}')
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_ENT_ID, ERN, ENTERPRISE, PERIOD)

    def test_reu_breadcrumb(self):
        self.search_by_unit_id_type_period(RURN, REPORTING_UNIT, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{REPORTING_UNIT}/units/{RURN}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'REU - {RURN}')
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_ENT_ID, ERN, ENTERPRISE, PERIOD)

    def test_leu_breadcrumb(self):
        self.search_by_unit_id_type_period(UBRN, LEGAL_UNIT, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{LEGAL_UNIT}/units/{UBRN}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'LEU - {UBRN}')
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_ENT_ID, ERN, ENTERPRISE, PERIOD)

    def test_ch_breadcrumb(self):
        self.search_by_unit_id_type_period(CRN, COMPANY_HOUSE, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{COMPANY_HOUSE}/units/{CRN}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'CRN - {CRN}')
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_ENT_ID, ERN, ENTERPRISE, PERIOD)
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_LEU_ID, UBRN, LEGAL_UNIT, PERIOD)

    def test_vat_breadcrumb(self):
        self.search_by_unit_id_type_period(VATREF, VALUE_ADDED_TAX, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{VALUE_ADDED_TAX}/units/{VATREF}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'VAT - {VATREF}')
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_ENT_ID, ERN, ENTERPRISE, PERIOD)
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_LEU_ID, UBRN, LEGAL_UNIT, PERIOD)

    def test_paye_breadcrumb(self):
        self.search_by_unit_id_type_period(PAYEREF, PAY_AS_YOU_EARN, '201810')
        self.assertEqual(self.driver.current_url, f'{SEARCH_URL}/periods/{PERIOD}/types/{PAY_AS_YOU_EARN}/units/{PAYEREF}')
        self.assert_breadcrumb_search_href()
        self.assert_current_breadcrumb_item_text(f'PAYE - {PAYEREF}')
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_ENT_ID, ERN, ENTERPRISE, PERIOD)
        self.assert_breadcrumb_item_text_and_url(BREADCRUMB_LEU_ID, UBRN, LEGAL_UNIT, PERIOD)


if __name__ == '__main__':
    unittest.main()
