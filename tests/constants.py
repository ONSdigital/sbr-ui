# This file contains any commonly used constants used within the Selenium tests
# e.g. button/input IDs, URLs etc.

# Authentication
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'
INVALID_USERNAME = 'abc'
INVALID_PASSWORD = 'abc'

# Input IDs
USERNAME_INPUT_ID = 'usernameInput'
PASSWORD_INPUT_ID = 'passwordInput'
SEARCH_INPUT_ID = 'referenceNumberInput'
LOGIN_BUTTON_ID = 'loginButton'
LOGOUT_BUTTON_ID = 'logoutButton'
SEARCH_BUTTON_ID = 'searchButton'

# Text IDs
HOME_TITLE_ID = 'homeTitle'
LOGIN_TITLE_ID = 'loginTitle'
SBR_DESCRIPTION_ID = 'sbrDescriptionText'

# URLs
PROTOCOL = 'http'
PORT = '5000'
HOST_NAME = 'localhost'
BASE_URL = f'{PROTOCOL}://{HOST_NAME}:{PORT}'
HOME_URL = f'{BASE_URL}/Home'
ERROR_URL = f'{BASE_URL}/Error'

# Search
PERIOD = '201810'
ENTREF = '1'
UBRN = '2'
LURN = '3'
CRN = '4'
PAYEREF = '5'
VATREF = '6'

