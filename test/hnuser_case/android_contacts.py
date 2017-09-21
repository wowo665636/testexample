import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from test.page.loginAnPage import Login


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class ContactsAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.2'
        desired_caps['deviceName'] = 'MI 3'
        # desired_caps['app'] = PATH('../../../sample-code/apps/ContactManager/ContactManager.apk')
        desired_caps['appPackage'] = 'com.palm.hno2o'
        desired_caps['appActivity'] = 'com.palm.hno2o.ui.NewMainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test0(self, username='18310094090', password='qqqqqq'):
        Login(self.driver).user_login(username, password)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)