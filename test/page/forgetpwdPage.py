from selenium.webdriver.common.by import By
from test.common.page import Page
from time import sleep


class fpwd_h5(Page):
    login_findpwd_log = (By.LINK_TEXT, '忘记密码?')

    def forgetpwd(self, username):
        self.find_element(*self.login_findpwd_log).click()

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_btn_loc).click()

    # 定义统一登录入口
    def user_login(self, username='42010003', password='qqqqqq'):
        """获取的用户名密码登录"""
        sleep(3)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)