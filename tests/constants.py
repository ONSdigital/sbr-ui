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
SEARCH_TITLE_ID = 'homeTitle'
LOGIN_TITLE_ID = 'loginTitle'
SBR_DESCRIPTION_ID = 'sbrDescriptionText'

# Breadcrumb IDs
BREADCRUMB_SEARCH_ID = 'breadcrumbSearchLink'
BREADCRUMB_SELECTED_ID = 'breadcrumbCurrentUnit'
BREADCRUMB_ENT_ID = 'breadcrumbEnt'
BREADCRUMB_LEU_ID = 'breadcrumbLeu'

# Child Links IDs
CHILD_LINKS_TABS_ID = 'childLinksTabs'
LEU_TAB = 'leuTab'
LOU_TAB = 'louTab'
CH_TAB = 'chTab'
VAT_TAB = 'vatTab'
PAYE_TAB = 'payeTab'
LEU_CHILD_TABLE = 'leuChildLinksTable'
LOU_CHILD_TABLE = 'louChildLinksTable'
CH_CHILD_TABLE = 'chChildLinksTable'
VAT_CHILD_TABLE = 'vatChildLinksTable'
PAYE_CHILD_TABLE = 'payeChildLinksTable'

# Unit Page Content
UNIT_NAME_ID = 'unitName'
UNIT_BADGE_ID = 'unitBadge'
UNIT_ID_ID = 'unitId'

# URLs
PROTOCOL = 'http'
PORT = '5000'
HOST_NAME = 'localhost'
BASE_URL = f'{PROTOCOL}://{HOST_NAME}:{PORT}'
LOGIN_URL = f'{BASE_URL}/Login'
SEARCH_URL = f'{BASE_URL}/Search'
ERROR_URL = f'{BASE_URL}/Error'

# Search
PERIOD = '201810'
ENTREF = '1'
UBRN = '2'
LURN = '3'
CRN = '4'
PAYEREF = '5'
VATREF = '6'



