from selenium import webdriver
import unittest
import time
from Pages.homePage import homePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_home_check_logo(self):
        self.driver.get("https://www.kwili.fr/")

        home = homePage(self.driver)
        home.check_logo()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
