import unittest
from time import sleep
from utils.log import logger
from selenium import webdriver
from test.page.loginPage import login_h5
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH


class LoginH5Tests(unittest.TestCase):
    URL = Config().get('URL')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = login_h5(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test0(self):
        self.sub_setUp()
        self.page.user_login()
        sleep(2)
        link = self.page.login_seccess
        logger.info(link.text)
        self.sub_tearDown()


if __name__ == '__main__':
    unittest.main()