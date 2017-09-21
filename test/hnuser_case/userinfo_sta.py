import unittest
from utils.config import Config
from test.page.sidebarPage import sidebar
from test.common import androidmyunit
from test.common.browser import Browser
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH


class userinfoTests(androidmyunit.MyTest):
    realname = Config().get('hnrealname')
    usercard = Config().get('hnusercard')

    def test0(self):
        po = sidebar(self.driver)
        link = po.userinfo_status().text
        print(link)
        if self.assertEqual(link, "未认证"):
            po.userinfo_status().click()
            sidebar(self.driver).userinfo(realname=self.realname, usercard=self.usercard)
            Browser.save_screen_shot(name='userinfo_seccess')    # 截图
        else:
            po.sidebar_btn()
            print(link)


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='湖北站主H5测试报告', description='修改html报告')
        runner.run(userinfoTests('test_login'))
