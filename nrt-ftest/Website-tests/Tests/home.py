import unittest
from Pages.HomePage import HomePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/"

    def test_01_home_check_logo(self):
        self.driver.get(self.url)

        home = HomePage(self.driver)
        home.check_logo()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()