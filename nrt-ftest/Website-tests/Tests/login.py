import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LandingPage import LandingPage
from Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.url = "https://localhost/"

    def test_01_login_valid(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_login()
        login = LoginPage(self.driver)
        login.login("jean-baptiste.melet@epitech.eu", "azertyuiop")

    def test_02_login_no_email_and_no_pwd(self):
        error_msg = "Erreur : email manquant. Veuillez entrer votre adresse mail."
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_login()
        login = LoginPage(self.driver)
        login.click_login()
        self.assertEqual(login.check_error(error_msg), error_msg)

    def test_03_login_pwd_but_no_email(self):
        error_msg = "Erreur : email manquant. Veuillez entrer votre adresse mail."
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_login()
        login = LoginPage(self.driver)
        login.enter_password("azertyuiop")
        login.click_login()
        self.assertEqual(login.check_error(error_msg), error_msg)

    def test_04_login_email_but_no_pwd(self):
        error_msg = "Erreur : mot de passe manquant. Veuillez entrer votre mot de passe."
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_login()
        login = LoginPage(self.driver)
        login.enter_username("jean-baptiste.melet@epitech.eu")
        login.click_login()
        self.assertEqual(login.check_error(error_msg), error_msg)

    # def test_05_login_invalid(self):
    #     error_msg = "Erreur : email et/ou mot de passe invalide."
    #     self.driver.get(self.url)
    #
    #     landing = LandingPage(self.driver)
    #     landing.click_login()
    #     login = LoginPage(self.driver)
    #     login.login("invalide.user@failtest.fr", "invalidpwd")
    #     login.click_login()
    #     login.check_error("Erreur : email et/ou mot de passe invalide.")
    #     self.assertEqual(login.check_error(error_msg), error_msg)

    def test_06_login_go_on_register(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_login()
        login = LoginPage(self.driver)
        login.click_register()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
