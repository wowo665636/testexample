import unittest
from time import sleep
from utils.log import logger
from selenium import webdriver
from test.page.loginPage import login_h5
from test.common import myunit
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH


class LoginH5Tests(myunit.MyTest):
    URL = Config().get('URL')
    USER = Config().get('stationname')
    PWD = Config().get('stationpwd')

    def test0(self):
        """正确登录"""
        driver = myunit.MyTest.sub_setUp(self)
        po = login_h5(driver)
        # po = login_h5(sub_setUp(self))
        po.user_login(username=self.USER, password=self.PWD)
        link = po.login_seccess().text
        self.assertEqual(link, "站主，您好！")
        po.save_screen_shot(name='login_seccess')  # 截图
        logger.info(link)
    """
    def test1(self):
        '''用户名为空'''
        po = login_h5()
        po.user_login(username="", password=self.PWD)
        link = po.user_result()
        po.save_screen_shot(name='username_error')  # 截图
        logger.info(link.text)
        self.sub_tearDown()
    """


if __name__ == '__main__':
    unittest.main()