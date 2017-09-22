import unittest

from test.stationhub_page.loginPage import login_h5
from utils.config import Config
from utils.log import logger


class LoginH5Tests(unittest.TestCase):
    URL = Config().get('URL')
    USER = Config().get('stationname')
    PWD = Config().get('stationpwd')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = login_h5(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        self.page.quit()

    def test0(self):
        """正确登录"""
        self.sub_setUp()
        self.page.user_login(username=self.USER, password=self.PWD)
        link = self.page.login_seccess().text
        self.assertEqual(link, "站主，您好！")
        self.page.save_screen_shot(name='login_seccess')  # 截图
        logger.info(link)
        self.sub_tearDown()

    def test1(self):
        """用户名为空"""
        self.sub_setUp()
        self.page.user_login(username="", password=self.PWD)
        link = self.page.user_result()
        self.page.save_screen_shot(name='username_error')  # 截图
        logger.info(link.text)
        self.sub_tearDown()


if __name__ == '__main__':
    unittest.main()