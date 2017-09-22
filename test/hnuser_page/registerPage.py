from selenium.webdriver.common.by import By
from test.common.androidpage import Page
from time import sleep


class register(Page):
    """注册页面"""
    register_user_loc = (By.ID, 'com.palm.hno2o:id/phone_num_et')
    register_codebtn_loc = (By.ID, 'com.palm.hno2o:id/time_tv')
    register_code_loc = (By.ID, 'com.palm.hno2o:id/code_et')
    register_pwd_loc = (By.ID, 'com.palm.hno2o:id/pwd_et')
    register_pwdok_loc = (By.ID, 'com.com.palm.hno2o:id/pwd_ok_et')
    register_read_loc = (By.ID, 'com.palm.hno2o:id/read_cb')
    register_submit_loc = (By.ID, 'com.palm.hno2o:id/submit_btn')

    def register_username(self, username):
        self.find_element(*self.register_user_loc).sendkeys(username)

    def register_code(self, code):
        self.find_element(*self.register_code_loc).sendkeys(code)

    def register_pwd(self, pwd):
        self.find_element(*self.register_pwd_loc).sendkeys(pwd)
        self.find_element(*self.register_pwdok_loc).sendkeys(pwd)

    def user_register(self, username='', code='', pwd=''):
        self.register_username(username)
        self.find_element(*self.register_codebtn_loc).click()
        sleep(2)
        self.register_code(code)
        self.register_pwd(pwd)
        self.find_element(*self.register_submit_loc).click()


