from selenium.webdriver.common.by import By
from test.common.androidpage import Page
from time import sleep


class SSQPage(Page):
    """双色球页面"""
    ssq_redball_loc = (By.XPATH, 'android.widget.TextView[@text="普通"]')
