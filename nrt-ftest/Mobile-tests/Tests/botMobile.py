import unittest
from appium import webdriver

from Screens.BotScreen import BotScreen
from Screens.LoginScreen import LoginScreen
from Screens.MapScreen import MapScreen


class BotMobileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r"C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile-tests\app-release.apk"}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_01_bot(self):
        login_screen = LoginScreen(self.driver)
        login_screen.click_login()
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()
        bot_screen = BotScreen(self.driver)
        bot_screen.click_bot_tab()
        bot_screen.send_text("Bonjour j'ai besoin d'assistance")
        bot_screen.send_text("Je crois que je me suis pété un orteil")
        bot_screen.send_text("Allo ?")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.driver.close()
