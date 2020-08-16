import unittest
from appium import webdriver

from Mobile_tests.Screens.BotScreen import BotScreen
from Mobile_tests.Screens.MapScreen import MapScreen


class BotMobileTest(unittest.TestCase):
    """
    Classe BotMobileTest.

    Teste les différents élements de l'écran du chat.
    """
    @classmethod
    def setUpClass(cls):
        """Charge le driver et l'émulateur."""
        desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r"C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile-tests\app-release.apk"}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_01_bot(self):
        """Teste l'envoie de messages vers le chat bot."""
        map_screen = MapScreen(self.driver)
        map_screen.click_allow_geo()
        bot_screen = BotScreen(self.driver)
        bot_screen.click_bot_tab()
        bot_screen.send_text("Bonjour j'ai besoin d'assistance")
        bot_screen.send_text("Je crois que je me suis cassé un orteil")
        bot_screen.send_text("Allo ?")

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.quit()