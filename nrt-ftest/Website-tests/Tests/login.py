from selenium import webdriver
import unittest
import time
from Pages.landingPage import landingPage
from Pages.loginPage import loginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_login_valid(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.login("jean-baptiste.melet@epitech.eu", "azertyuiop")

    def test_02_login_no_email_and_no_pwd(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.click_login()
        self.assertEqual(login.check_error(), "Erreur : email manquant. Veuillez entrer votre adresse mail.")

    def test_03_login_pwd_but_no_email(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.enter_password("azertyuiop")
        login.click_login()
        self.assertEqual(login.check_error(), "Erreur : email manquant. Veuillez entrer votre adresse mail.")

    def test_04_login_email_but_no_pwd(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.enter_username("jean-baptiste.melet@epitech.eu")
        login.click_login()
        self.assertEqual(login.check_error(), "Erreur : mot de passe manquant. Veuillez entrer votre mot de passe.")

    def test_05_login_invalid(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.login("invalide.user@failtest.fr", "invalidpwd")
        login.click_login()
        time.sleep(3)
        self.assertEqual(login.check_error(), "Erreur : email et/ou mot de passe invalide.")

    def test_06_login_go_on_register(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_login()
        login = loginPage(self.driver)
        login.click_register()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
