import unittest
from time import sleep

from appium import webdriver
from Mobile_tests.Screens.TutoScreen import TutoScreen
from Mobile_tests.Screens.ContactScreen import ContactScreen


class ContactMobileTest(unittest.TestCase):
    """
    Classe BotMobileTest.

    Teste les différents élements de l'écran settings.
    """

    @classmethod
    def setUpClass(cls):
        """Charge le driver et l'émulateur."""
        desired_caps = {'platformName': 'Android', 'platformVersion': '11.0', 'automationName': 'uiautomator2',
                        'deviceName': 'Android Emulator',
                        'app': r'C:\Users\prato\Documents\Courses\Epitech\NRT-FTEST\nrt-ftest\Mobile_tests\app-release.apk'}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5000)

    def test_contact_send(self):
        """Teste les boutons de l'écran settings."""
        tuto_screen = TutoScreen(self.driver)
        tuto_screen.button_click("SUIVANT")
        tuto_screen.button_click("SUIVANT")
        tuto_screen.button_click("QUITTER LE TUTORIEL")
        contact = ContactScreen(self.driver)
        contact.click_contact_tab()
        contact.write_name("Kentin")
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.quit()
