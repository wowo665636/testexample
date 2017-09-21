
class Page(object):
    """
    页面基础类，用于所有页面的继承
    """
    def __init__(self, selenium_driver, parent=None):
        self.driver = selenium_driver
        self.parent = parent

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):                        # 定义多个元素
        return self.driver.find_elements(*loc)

    def script(self, src):
        return self.driver.execute_script(src)    # 调用 javascript代码
