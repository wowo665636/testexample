import os
import unittest
from appium import webdriver
from utils.config import Config

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class MyTest(unittest.TestCase):
    appPackage = Config().get('appPackage')
    appActivity = Config().get('appActivity')

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.2'
        desired_caps['deviceName'] = 'MI 3'
        # desired_caps['app'] = PATH('../../../sample-code/apps/ContactManager/ContactManager.apk')
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
