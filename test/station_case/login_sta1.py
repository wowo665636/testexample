# coding=utf-8
from test.common import myunit
from test.stationhub_page.loginPage import login_h5
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import Config, REPORT_PATH
from utils.log import logger


class LoginH5Tests(myunit.MyTest):
    URL = Config().get('HuBURL')
    USER = Config().get('stationname')
    PWD = Config().get('stationpwd')

    def test0(self):
        """正确登录"""
        po = login_h5(self.driver)
        # po = login_h5(sub_setUp(self))
        po.user_login(username=self.USER, password=self.PWD)
        link = po.login_seccess().text
        self.assertEqual(link, "站主，您好！")
        po.save_screen_shot(name='login_seccess')  # 截图
        logger.info(link)

    def test1(self):
        """用户名为空"""
        po = login_h5(self.driver)
        po.user_login(username="", password=self.PWD)
        link = po.user_result()
        po.save_screen_shot(name='username_error')  # 截图
        logger.info(link.text)


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='湖北站主H5测试报告', description='修改html报告')
        runner.run(LoginH5Tests('test0'))
