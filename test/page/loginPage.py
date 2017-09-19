from selenium.webdriver.common.by import By
from test.common.page import Page
from time import sleep


class login_h5(Page):
    login_username_loc = (By.ID, 'user_name')
    login_password_loc = (By.ID, 'user_password')
    login_btn_loc = (By.CLASS_NAME, 'login_btn')
    login_seccess_log = (By.CLASS_NAME, 'ng-binding')

    user_result_log = (By.XPATH, 'html/body/div[1]/section/ul/li[1]/p')
    pwd_result_log = (By.XPATH, 'html/body/div[1]/section/ul/li[2]/p')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_btn_loc).click()

    # 定义统一登录入口
    def user_login(self, username='', password=''):
        """获取的用户名密码登录"""
        sleep(3)
        self.login_username(username)
        self.login_password(password)
        self.execute("window.scrollTo(0,800)")   # 设置浏览器窗口滚动条的位置，execute也可以调用js
        self.login_button()
        sleep(1)

    def user_result(self):
        return self.find_element(*self.user_result_log)

    def pwd_result(self):
        return self.find_element(*self.pwd_result_log)

    def login_seccess(self):
        return self.find_element(*self.login_seccess_log)