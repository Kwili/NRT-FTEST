import unittest
from Pages.LandingPage import LandingPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LandingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://localhost/"

    def test_01_check_all_images_on_the_landingPage(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.check_all_images()

    def test_02_check_login_button(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_login()

    def test_03_check_register_button(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()

    def test_04_check_map_button(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_map()

    def test_05_check_info_button(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_info()

    def test_06_contact_us(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.contact_us("testing", "test.person@testing.fr", "TEST automate", "ceci est un test")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
