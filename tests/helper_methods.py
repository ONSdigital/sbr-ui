import os
import collections

from selenium.webdriver.firefox.options import Options


def flatten(d, parent_key='', sep='_'):
    """ https://stackoverflow.com/a/6027615 """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def create_selenium_config():
    """ If the SELENIUM_HEADLESS environment variable is True, run Selenium in headless mode. """
    options = Options()
    if os.environ.get('SELENIUM_HEADLESS'):
        options.add_argument("--headless")
    return options
