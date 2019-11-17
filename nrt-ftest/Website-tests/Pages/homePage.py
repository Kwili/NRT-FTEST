from .landingPage import landingPage
from .loginPage import loginPage
import time

class homePage():

    def __init__(self, driver):
        self.driver = driver

        self.logo_xpath         = "//*[@id=\"root\"]/div/div/div[2]/nav/a/img"

    def check_logo(self):
        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.login("jean-baptiste.melet@epitech.eu", "azertyuiop")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.logo_xpath)
