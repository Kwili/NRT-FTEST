import unittest
from Pages.LandingPage import LandingPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LandingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/landing"

    def test_check_navbar(self):
        self.driver.get(self.url)
        landing = LandingPage(self.driver)
        home_url = self.url[:-7]

        landing.click_home()
        self.assertEqual(self.driver.current_url, home_url)
        self.driver.get(self.url)

        landing.click_map()
        self.assertEqual(self.driver.current_url, f"{home_url}map")
        self.driver.get(self.url)

        landing.click_app_link()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
