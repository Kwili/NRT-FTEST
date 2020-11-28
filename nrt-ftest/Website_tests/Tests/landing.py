import unittest
from Website_tests.Pages.LandingPage import LandingPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LandingTest(unittest.TestCase):
    """
    Classe LandingTest.

    Teste les différents élements de la page /landing.
    """
    @classmethod
    def setUpClass(cls):
        """Charge le drive Chrome."""
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.driver.implicitly_wait(5)
        cls.url = "https://www.kwili.fr/landing"

    def test_check_navbar(self):
        """
        Testes les différents boutons de la navbar.
        """
        self.driver.get(self.url)
        landing = LandingPage(self.driver)
        home_url = self.url[:-7]

        # Check home button
        landing.click_home()
        self.assertEqual(self.driver.current_url, home_url)
        self.driver.get(self.url)

        # Check map button
        landing.click_map()
        self.assertEqual(self.driver.current_url, f"{home_url}map")
        self.driver.get(self.url)

        # Check app button
        landing.click_navbar_app_link()
        windows = self.driver.window_handles
        self.assertEqual(2, len(windows))
        self.driver.switch_to.window(windows[1])
        self.assertEqual(self.driver.current_url, "https://play.google.com/store/apps/details?id=fr.kwili.kwili")
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    def test_apercu(self):
        """
        Teste la section aperçu.
        """
        self.driver.get(self.url)
        landing = LandingPage(self.driver)

        # Check app link
        landing.click_app_apercu_link()
        windows = self.driver.window_handles
        self.assertEqual(2, len(windows))
        self.driver.switch_to.window(windows[1])
        self.assertEqual(self.driver.current_url, "https://play.google.com/store/apps/details?id=fr.kwili.kwili")
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    def test_chat_landing(self):
        """
        Teste le chat widget de la landing page.
        """
        self.driver.get(self.url)
        landing = LandingPage(self.driver)

        landing.click_chat_widget()

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.close()
        cls.driver.quit()
