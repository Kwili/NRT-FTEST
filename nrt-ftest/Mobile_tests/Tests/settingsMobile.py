import unittest
from appium import webdriver

from Mobile_tests.Screens.TutoScreen import TutoScreen
from Mobile_tests.Screens.SettingsScreen import SettingsScreen


class SettingsMobileTest(unittest.TestCase):
    """
    Classe BotMobileTest.

    Teste les différents élements de l'écran du chat.
    """

    @classmethod
    def setUpClass(cls):
        """Charge le driver et l'émulateur."""
        desired_caps = {'platformName': 'Android', 'platformVersion': '11.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r"C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile_tests\app-release.apk"}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_settings(self):
        """Teste l'envoie de messages vers le chat bot."""
        tuto_screen = TutoScreen(self.driver)
        tuto_screen.button_click("SUIVANT")
        tuto_screen.button_click("SUIVANT")
        tuto_screen.button_click("QUITTER LE TUTORIEL")
        settings_screen = SettingsScreen(self.driver)
        settings_screen.click_settings_tab()
        settings_screen.click_cursor("OFF")

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.quit()
