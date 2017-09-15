from selenium.webdriver.common.by import By
from test.common.page import Page
from time import sleep


class login_h5(Page):
    login_username_loc = (By.ID, 'user_name')
    login_password_loc = (By.ID, 'user_password')
    login_btn_loc = (By.ID, 'login_btn')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

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