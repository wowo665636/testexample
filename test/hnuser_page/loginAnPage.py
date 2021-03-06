from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test.common.androidpage import Page
from time import sleep


class Login(Page):
    """首页"""
    # Action从首页点击登录按钮，进入到登录页面
    home_index_loc = (By.ID, 'com.palm.hno2o:id/rb_index')
    home_myorder_loc = (By.ID, 'com.palm.hno2o:id/my_order')

    # 首页按钮
    def home_index(self):
        self.find_element(*self.home_index_loc).click()

    # 我的方案
    def home_myorder(self):
        self.find_element(*self.home_myorder_loc).click()
    # 选号
    lottery_btn_loc = (By.ID, 'com.palm.hno2o:id/stake_lotter')
    lottery_SSQ_loc = (By.ID, 'com.palm.hno2o:id/lottery_ssq_rl')
    lottery_QLC_loc = (By.ID, 'com.palm.hno2o:id/lottery_qlc_rl')
    lottery_D3_loc = (By.ID, 'com.palm.hno2o:id/lottery_3d_rl')
    lottery_HBP3_loc = (By.ID, 'com.palm.hno2o:id/lottery_k3_rl')
    lottery_C225_loc = (By.ID, 'com.palm.hno2o:id/lottery_c30s5_rl')

    def lottery_btn(self):
        self.find_element(*self.lottery_btn_loc).click()

    def lottery_ssq(self):
        self.find_element(*self.lottery_SSQ_loc).click()

    """用户登录界面"""
    login_username_loc = (By.ID, 'com.palm.hno2o:id/login_username_et')
    login_userpwd_loc = (By.ID, 'com.palm.hno2o:id/login_userpwd_et')
    login_btn_loc = (By.ID, 'com.palm.hno2o:id/btn_login')

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
        sleep(5)
        self.swipeUp(1000)
        self.home_myorder()

        self.login_username(username)
        self.login_userpwd(password)
        self.login_button()
        sleep(12)

    login_register_loc = (By.ID, 'com.palm.hno2o:id/btn_register')
    login_forget_loc = (By.ID, 'com.palm.hno2o:id/forget_cb')

    def register(self):
        self.find_elements(*self.login_register_loc).click()

    def forget(self):
        self.find_elements(*self.login_forget_loc).click()

