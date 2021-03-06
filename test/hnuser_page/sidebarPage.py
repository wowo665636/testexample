# coding=utf-8
from selenium.webdriver.common.by import By
from test.common.androidpage import Page
from time import sleep


class sidebar(Page):
    """侧边栏"""
    sidebar_btn_loc = (By.CLASS_NAME, 'android.widget.ImageButton')

    def sidebar_btn(self):
        self.find_element(*self.sidebar_btn_loc).click()

    nav_userinfo_loc = (By.NAME, '个人资料')
    nav_userpwd_loc = (By.NAME, '密码修改')
    nav_setting_loc = (By.NAME, '我的设置')
    nav_myorder_loc = (By.ID, 'com.palm.hno2o:id/my_order')

    # 个人资料
    def nav_userinfo(self):
        self.find_element(*self.nav_userinfo_loc).click()

    userinfo_loc = (By.ID, 'com.palm.hno2o:id/user_info_tv')

    def userinfo_status(self):
        self.find_elements(*self.userinfo_loc)

    realname_loc = (By.ID, 'com.palm.hno2o:id/name_et')
    usercard_loc = (By.ID, 'com.palm.hno2o:id/card_et')
    submit_loc = (By.ID, 'com.palm.hno2o:id/submit_btn')

    def userinfo(self, realname='', usercard=''):
        self.find_elements(*self.realname_loc).sendkeys(realname)
        self.find_elements(*self.usercard_loc).sendkeys(usercard)
        self.find_elements(*self.submit_loc).click()

    # 密码修改
    def nav_userpwd(self):
        self.find_element(*self.nav_userpwd_loc).click()

    now_pwd_loc = (By.ID, 'com.palm.hno2o:id/now_pwd_et')
    new_pwd1_loc = (By.ID, 'com.palm.hno2o:id/pwd1_et')
    new_pwd2_loc = (By.ID, 'com.palm.hno2o:id/pwd2_et')

    def modifypwd(self, nowpwd, newpwd):
        self.find_element(*self.now_pwd_loc).sendkeys(nowpwd)
        self.find_element(*self.new_pwd1_loc).sendkeys(newpwd)
        self.find_element(*self.new_pwd2_loc).sendkeys(newpwd)
        self.find_elements(*self.submit_loc).click()

