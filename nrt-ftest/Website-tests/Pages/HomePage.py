import time
from .LandingPage import LandingPage
from .LoginPage import LoginPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logo_xpath = "//*[@id=\"root\"]/div/div/div[2]/nav/a/img"

    def check_logo(self):
        landing = LandingPage(self.driver)
        landing.click_login()
        login = LoginPage(self.driver)
        login.login("jean-baptiste.melet@epitech.eu", "azertyuiop")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.logo_xpath)
