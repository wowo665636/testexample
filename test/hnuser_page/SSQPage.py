from selenium.webdriver.common.by import By
from test.common.androidpage import Page
from time import sleep


class SSQPage(Page):
    """双色球页面"""
    ssq_pt_loc = (By.NAME, '普通')
    ssq_dt_loc = (By.NAME, '胆拖')
    ssq_redball_loc = (By.AccessibilityId, 'ball_0_13')
