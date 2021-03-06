import time
from test.common import androidmyunit
from test.common.browser import Browser
from test.hnuser_page.sidebarPage import sidebar
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import Config, REPORT_PATH


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
            Browser.save_screen_shot(name='userinfo_fail')  # 截图
            po.sidebar_btn()
            print(link)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report = REPORT_PATH + '/' + now + 'report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='湖北站主H5测试报告', description='用例执行情况：')
        runner.run(userinfoTests('test0'))
