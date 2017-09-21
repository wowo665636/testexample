import unittest
from utils.config import Config
from test.page.loginAnPage import Login
from test.common import androidmyunit


class ContactsAndroidTests(androidmyunit.MyTest):
    username = Config().get('hnusername')
    password = Config().get('hnpassword')

    def test0(self, username=username, password=password):
        Login(self.driver).user_login(username, password)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
