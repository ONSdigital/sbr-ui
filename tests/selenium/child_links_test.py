import unittest
from selenium import webdriver

from tests.helper_methods import create_selenium_config

from tests.constants import BASE_URL
from tests.constants import CHILD_LINKS_TABS_ID, LEU_TAB, LU_TAB, CH_TAB, PAYE_TAB, VAT_TAB
from tests.constants import LEU_CHILD_TABLE, LU_CHILD_TABLE, CH_CHILD_TABLE, VAT_CHILD_TABLE, PAYE_CHILD_TABLE
from tests.constants import SEARCH_BUTTON_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, SEARCH_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ENTREF, UBRN, LURN, VATREF, PAYEREF, CRN, PERIOD
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD


class ChildLinksTest(unittest.TestCase):
    """ TODO: test that the number of units of a certain type is correct (need to make more test data) """

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

    def assert_tab_is_selected(self, tab_id):
        tab = self.driver.find_element_by_id(tab_id)
        tab_class_name = tab.get_attribute('class')
        self.assertEqual(tab_class_name, 'active')

    def assert_child_links_table_urls(self, child_table_id, unit_type, unit_id):
        """ TODO: update this method to handle multiple child links in each table """
        self.search_by_unit_id(ENTREF)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/ENT/units/{ENTREF}')
        child_table = self.driver.find_element_by_id(child_table_id)
        url = child_table.find_elements_by_tag_name('a')[0].get_attribute('href')
        self.assertEqual(url, f'{BASE_URL}/api/periods/{PERIOD}/types/{unit_type}/units/{unit_id}')

    def assert_tabs_length_and_return_tabs(self, num_tabs, selected_tab):
        child_link_tabs = self.driver.find_element_by_id(CHILD_LINKS_TABS_ID)
        tabs = child_link_tabs.find_elements_by_tag_name('li')
        self.assertEqual(len(tabs), num_tabs)
        self.assert_tab_is_selected(selected_tab)
        return tabs

    def test_changing_tabs_ent(self):
        self.search_by_unit_id(ENTREF)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/ENT/units/{ENTREF}')
        tabs = self.assert_tabs_length_and_return_tabs(5, LEU_TAB)
        tab_ids = [LEU_TAB, LU_TAB, CH_TAB, PAYE_TAB, VAT_TAB]  # Actual order of tabs
        expected_tabs_text = ['LEU (1)', 'LU (1)', 'CRN (1)', 'PAYE (1)', 'VAT (1)']  # Expected tab text
        for tab, tab_id, expected_tab_text in zip(tabs, tab_ids, expected_tabs_text):
            tab.click()
            self.assert_tab_is_selected(tab_id)
            self.assertEqual(tab.text, expected_tab_text)

    def test_changing_tabs_leu(self):
        self.search_by_unit_id(UBRN)
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/LEU/units/{UBRN}')
        tabs = self.assert_tabs_length_and_return_tabs(3, CH_TAB)
        tab_ids = [CH_TAB, PAYE_TAB, VAT_TAB]  # Actual order of tabs
        expected_tabs_text = ['CRN (1)', 'PAYE (1)', 'VAT (1)']  # Expected tab text
        for tab, tab_id, expected_tab_text in zip(tabs, tab_ids, expected_tabs_text):
            tab.click()
            self.assert_tab_is_selected(tab_id)
            self.assertEqual(tab.text, expected_tab_text)

    def test_leu_child_table_links(self):
        self.assert_child_links_table_urls(LEU_CHILD_TABLE, 'LEU', UBRN)

    def test_lu_child_table_links(self):
        self.assert_child_links_table_urls(LU_CHILD_TABLE, 'LU', LURN)

    def test_ch_child_table_links(self):
        self.assert_child_links_table_urls(CH_CHILD_TABLE, 'CH', CRN)

    def test_vat_child_table_links(self):
        self.assert_child_links_table_urls(VAT_CHILD_TABLE, 'VAT', VATREF)

    def test_paye_child_table_links(self):
        self.assert_child_links_table_urls(PAYE_CHILD_TABLE, 'PAYE', PAYEREF)


if __name__ == '__main__':
    unittest.main()
