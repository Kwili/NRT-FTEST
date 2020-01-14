import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LandingPage import LandingPage
from Pages.RegisterPage import RegisterPage


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "http://localhost:80/"

    def test_01_invalid_resgister_all_fileds_ared_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_02_register(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()

    def test_03_register_pwd_are_differents(self):
        error_msg = "Erreur: veuillez entrer le même mot de passe."
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "azertyuiop", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_04_register_name_is_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."

        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("", "person", "20081999", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_05_resgister_last_name_is_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "", "20081999", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_06_register_date_is_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."

        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "person", "", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_07_register_mail_is_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."

        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "person", "20081999", "", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_08_register_pwd_is_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."

        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_09_register_confirm_pwd_is_empty(self):
        error_msg = "Erreur: un ou plusieurs champs n'ont pas été remplis."

        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "", "patient")
        register.click_register()
        self.assertEqual(register.check_error(error_msg), error_msg)

    def test_11_already_registered(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_register()
        register = RegisterPage(self.driver)
        register.click_already_registered()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
