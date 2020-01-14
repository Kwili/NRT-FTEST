import unittest
from appium import webdriver
from Screens.RegisterScreen import RegisterScreen


class RegisterMobileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r"C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile-tests\app-release.apk"}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_01_Bad_Email(self):
        register_screen = RegisterScreen(self.driver)
        register_screen.click_register()
        register_screen.click_patient()
        register_screen.fill_email("bad email")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     # cls.driver.close()
