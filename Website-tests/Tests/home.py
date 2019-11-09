from selenium import webdriver
import unittest
import time
from Pages.homePage import homePage

class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("chromedriver")

    def test_01_home_check_logo(self):
        self.driver.get("https://www.kwili.fr/")

        home = homePage(self.driver)
        home.check_logo()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
