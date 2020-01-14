import unittest
from appium import webdriver
from Screens.LoginScreen import LoginScreen
from Screens.MapScreen import MapScreen


class MapMobileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r"C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile-tests\app-release.apk"}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_01_map_feet(self):
        login_screen = LoginScreen(self.driver)
        login_screen.click_login()
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()
        map_screen.click_rechercher()
        map_screen.has_found_itinary()

    def test_02_map_car(self):
        self.driver.reset()
        login_screen = LoginScreen(self.driver)
        login_screen.click_login()
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()
        map_screen.click_transport()
        map_screen.choose_transport(2)
        map_screen.click_rechercher()
        map_screen.has_found_itinary()

    def test_03_map_adress_written(self):
        self.driver.reset()
        login_screen = LoginScreen(self.driver)
        login_screen.click_login()
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()
        map_screen.click_votre_position()
        map_screen.write_position("3 avenue montaigne paris")
        map_screen.click_rechercher()
        map_screen.has_found_itinary()

    def test_04_map_display_details(self):
        self.driver.reset()
        login_screen = LoginScreen(self.driver)
        login_screen.click_login()
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()
        map_screen.click_transport()
        map_screen.choose_transport(2)
        map_screen.click_rechercher()
        map_screen.click_plus()
        map_screen.click_najma()
        map_screen.click_return()
        map_screen.has_found_itinary()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.driver.close()
