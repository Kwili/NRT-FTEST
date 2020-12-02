import unittest
from time import sleep

from appium import webdriver
from Mobile_tests.Screens.BotScreen import BotScreen
from Mobile_tests.Screens.TutoScreen import TutoScreen


class BotMobileTest(unittest.TestCase):
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

    def test_msg(self):
        """Teste l'envoie de messages vers le chat bot."""
        tuto_screen = TutoScreen(self.driver)
        tuto_screen.button_click("SUIVANT")
        tuto_screen.button_click("SUIVANT")
        tuto_screen.button_click("QUITTER LE TUTORIEL")

        bot_screen = BotScreen(self.driver)
        bot_screen.send_text("J'ai mal")
        sleep(0.5)
        bot_screen.send_text("au pied")
        sleep(0.5)
        bot_screen.send_text("3")
        sleep(0.5)
        bot_screen.send_text("2 jours")
        sleep(0.5)
        bot_screen.send_text("oui")
        sleep(0.5)
        bot_screen.send_text("oui")
        sleep(0.5)
        bot_screen.send_text("184 cm")
        sleep(0.5)
        bot_screen.send_text("66 kg")
        sleep(0.5)
        bot_screen.send_text("non")
        sleep(0.5)
        bot_screen.send_text("Poils de chats")
        sleep(0.5)
        bot_screen.send_text("0")
        sleep(0.5)
        bot_screen.send_text("oui")

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.quit()
