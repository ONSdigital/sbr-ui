import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from tests.constants import BASE_URL, ERROR_URL
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
        self.driver = webdriver.Firefox()
        self.driver.get(BASE_URL)
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(ADMIN_USERNAME)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(ADMIN_PASSWORD)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()

    def tearDown(self):
        self.driver.find_element_by_id(LOGOUT_BUTTON_ID).click()
        self.driver.quit()

    def test_search_input_focus(self):
        """ Ensure the search input has focus """
        search_input = self.driver.find_element_by_id(SEARCH_INPUT_ID)
        self.assertEqual(search_input, self.driver.switch_to.active_element)

    def test_header_text(self):
        """ Ensure the SBR description text that is present on login/home pages is no longer present. """
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(ENTREF)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_id(SBR_DESCRIPTION_ID)

    def test_search_ent(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(ENTREF)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/ENT/units/{ENTREF}')

    def test_search_lu(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(LURN)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/LU/units/{LURN}')

    def test_search_leu(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(UBRN)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/LEU/units/{UBRN}')

    def test_search_ch(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(CRN)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/CH/units/{CRN}')

    def test_search_vat(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(VATREF)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/VAT/units/{VATREF}')

    def test_search_paye(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys(PAYEREF)
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/periods/{PERIOD}/types/PAYE/units/{PAYEREF}')

    def test_unit_not_found(self):
        self.driver.find_element_by_id(SEARCH_INPUT_ID).send_keys('Tesco')
        self.driver.find_element_by_id(SEARCH_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, ERROR_URL)
        self.assertTrue('404 - Not Found' in self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
