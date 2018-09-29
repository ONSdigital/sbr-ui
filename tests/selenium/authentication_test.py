import unittest
from selenium import webdriver

from tests.constants import BASE_URL, HOME_URL, ERROR_URL
from tests.constants import LOGIN_TITLE_ID, HOME_TITLE_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD


class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_title = self.driver.find_element_by_id(LOGIN_TITLE_ID).text
        self.assertEqual(login_title, 'Sign in')
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(ADMIN_USERNAME)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(ADMIN_PASSWORD)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, HOME_URL)
        title = self.driver.find_element_by_id(HOME_TITLE_ID).text
        self.assertEqual(title, 'Search the UK business population')

    def test_login_and_logout(self):
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(ADMIN_USERNAME)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(ADMIN_PASSWORD)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, HOME_URL)
        home_title = self.driver.find_element_by_id(HOME_TITLE_ID).text
        self.assertEqual(home_title, 'Search the UK business population')
        self.driver.find_element_by_id(LOGOUT_BUTTON_ID).click()
        login_title = self.driver.find_element_by_id(LOGIN_TITLE_ID).text
        self.assertEqual(login_title, 'Sign in')

    def test_login_and_refresh(self):
        """ This is just to ensure the session continues after a refresh """
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(ADMIN_USERNAME)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(ADMIN_PASSWORD)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()
        home_title = self.driver.find_element_by_id(HOME_TITLE_ID).text
        self.assertEqual(home_title, 'Search the UK business population')
        self.assertEqual(self.driver.current_url, HOME_URL)
        self.driver.refresh()
        self.assertEqual(self.driver.current_url, HOME_URL)

    def test_private_routes(self):
        """ We need to ensure that an unauthenticated user cannot get past the login page """
        login_title = self.driver.find_element_by_id(LOGIN_TITLE_ID).text
        self.assertEqual(login_title, 'Sign in')
        self.driver.get(HOME_URL)
        self.assertTrue('401 - Not Authenticated' in self.driver.page_source)
        self.assertTrue('Please login before navigating to the Home or Results pages.' in self.driver.page_source)
        self.assertEqual(self.driver.current_url, ERROR_URL)

    def test_invalid_credentials(self):
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(INVALID_USERNAME)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(INVALID_PASSWORD)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()
        self.assertTrue('Invalid Credentials. Please try again.' in self.driver.page_source)
        # For some reason, Firefox shows the URL with a trailing '/'
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/')


if __name__ == '__main__':
    unittest.main()
