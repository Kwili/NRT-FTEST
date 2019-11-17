from selenium import webdriver
import unittest
import time
from Pages.landingPage import landingPage
from Pages.registerPage import registerPage
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_invalid_resgister_all_fileds_ared_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_02_register(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()

    def test_03_register_pwd_are_differents(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "azertyuiop", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: veuillez entrer le même mot de passe.")

    def test_04_register_name_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("", "person", "20081999", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_05_resgister_last_name_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "", "20081999", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_06_register_date_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "", "test.person@testing.fr", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_07_register_mail_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "20081999", "", "azerty", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_08_register_pwd_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "", "azerty", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_09_register_confirm_pwd_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "", "patient")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_10_register_person_type_is_empty(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.register("test", "person", "20081999", "test.person@testing.fr", "azerty", "azerty", "")
        register.click_register()
        self.assertEqual(register.check_error(), "Erreur: un ou plusieurs champs n'ont pas été remplis.")

    def test_11_already_registered(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_register()
        register = registerPage(self.driver)
        register.click_already_registered()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()