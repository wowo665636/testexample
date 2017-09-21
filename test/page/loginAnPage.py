from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test.common.androidpage import Page
from time import sleep


class Login(Page):
    """
    用户登录界面
    """
    # Action从首页点击登录按钮，进入到登录页面
    home_mycase_loc = (By.ID, 'com.palm.hno2o:id/my_order')

    # 我的方案
    def home_mycase(self):
        self.find_element(*self.home_mycase_loc).click()

    login_username_loc = (By.ID, 'com.palm.hno2o:id/login_username_et')
    login_userpwd_loc = (By.ID, 'com.palm.hno2o:id/login_userpwd_et')
    login_btn_loc = (By.ID, 'com.palm.hno2o:id/btn_login')
    login_register_loc = (By.ID, 'com.palm.hno2o:id/btn_register')
    login_forget_loc = (By.ID, 'com.palm.hno2o:id/forget_cb')

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_userpwd(self, password):
        self.find_element(*self.login_userpwd_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_btn_loc).click()

    # 定义统一登录入口
    def user_login(self, username='18310094090', password='qqqqqq'):
        """获取的用户名密码登录"""
        self.home_mycase()

        self.login_username(username)
        self.login_userpwd(password)
        self.login_button()
        sleep(12)

