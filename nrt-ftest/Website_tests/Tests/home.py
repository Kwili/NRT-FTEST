import unittest
from Website_tests.Pages.HomePage import HomePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HomeTest(unittest.TestCase):
    """
    Classe HomeTest.

    Teste les différents élements de la page d'accueil.
    """

    @classmethod
    def setUpClass(cls):
        """Charge le drive Chrome."""
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/"

    def test_chat_link(self):
        """teste le lien du chat."""
        self.driver.get(self.url)
        home = HomePage(self.driver)
        home.click_chat_card()
        self.assertEqual(self.driver.current_url, self.url)

    def test_map_link(self):
        """test le lien de la map."""
        self.driver.get(self.url)
        home = HomePage(self.driver)
        home.click_map_card()
        self.assertEqual(self.driver.current_url, f"{self.url}map")

    def test_landing_link(self):
        """teste le lien de la landing."""
        self.driver.get(self.url)
        home = HomePage(self.driver)
        home.click_landing_button()
        self.assertEqual(self.driver.current_url, f"{self.url}landing")

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.close()
        cls.driver.quit()
