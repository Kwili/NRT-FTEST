from selenium import webdriver
import unittest
from Pages.landingPage import landingPage
from Pages.loginPage import loginPage

class LandingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("chromedriver")

    def test_01_check_all_images_on_the_landingPage(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.check_all_images()

    def test_02_check_login_button(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()

    def test_03_check_register_button(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()

    def test_04_check_map_button(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_map()

    def test_05_check_info_button(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_info()

    def test_06_contact_us(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.contact_us("testing", "test.person@testing.fr", "TEST automate", "ceci est un test")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()