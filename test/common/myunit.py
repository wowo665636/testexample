import unittest
from utils.config import Config
from test.common.browser import Browser


class MyTest(unittest.TestCase):
    browser_type = Config().get('browser_type')
    URL = Config().get('URL')

    def setUp(self):
        self.driver = Browser(browser_type=self.browser_type).get(self.URL, maximize_window=True)

    def tearDown(self):
        self.driver.quit()