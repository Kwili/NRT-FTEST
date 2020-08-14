import unittest
from Website_tests.Pages.HomePage import HomePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HomeTest(unittest.TestCase):
    """Home Page Test."""

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/"

    def test_chat_link(self):
        """
        test chat link.
        """
        self.driver.get(self.url)
        home = HomePage(self.driver)
        home.click_chat_card()
        self.assertEqual(self.driver.current_url, self.url)

    def test_map_link(self):
        """
        test map link.
        """
        self.driver.get(self.url)
        home = HomePage(self.driver)
        home.click_map_card()
        self.assertEqual(self.driver.current_url, f"{self.url}map")

    def test_landing_link(self):
        """
        test landing link.
        """
        self.driver.get(self.url)
        home = HomePage(self.driver)
        home.click_landing_button()
        self.assertEqual(self.driver.current_url, f"{self.url}landing")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
