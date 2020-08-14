import unittest
from appium import webdriver
from Mobile_tests.Screens.LoginScreen import LoginScreen
from Mobile_tests.Screens.MapScreen import MapScreen


class LoginMobileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r"C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile-tests\app-release.apk"}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_01_No_Login(self):
        login_screen = LoginScreen(self.driver)
        login_screen.click_login()

    def test_02_Loggin(self):
        self.driver.reset()
        login_screen = LoginScreen(self.driver)
        login_screen.fill_id()
        login_screen.click_login()
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.driver.close()
