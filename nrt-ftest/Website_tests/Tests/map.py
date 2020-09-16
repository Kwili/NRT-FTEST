import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Website_tests.Pages.MapPage import MapPage


class MapTest(unittest.TestCase):
    """
    Classe MapTest.

    Teste les différents élements de la page /map.
    """
    @classmethod
    def setUpClass(cls):
        """Charge le drive Chrome."""
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/map"

    def test_find_itinary(self):
        """
        Teste l'itinéraire.

        Ecris l'adresse et clique sur les transports dispnibles.
        """
        self.driver.get(self.url)
        map_page = MapPage(self.driver)

        map_page.write_position("1 rue rivoli")
        self.assertTrue(map_page.is_hospital_displayed())
        map_page.click_bus()
        map_page.click_car()
        map_page.click_walk()

    def test_zoom(self):
        """
        Teste le zoom.

        Zoom de différentes valeurs.
        """
        self.driver.get(self.url)
        map_page = MapPage(self.driver)

        map_page.write_position("1 rue rivoli")
        map_page.zoom_in()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_out()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_in()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_in()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_in()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_out()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_in()
        sleep(0.4)
        # TODO: Remove sleep function
        map_page.zoom_out()

    def test_radius(self):
        """
        Test radius.

        Test le radius slider.
        """
        self.driver.get(self.url)
        map_page = MapPage(self.driver)

        map_page.write_position("1 rue rivoli")
        map_page.move_slider(150)
        map_page.move_slider(150)
        map_page.move_slider(150)
        map_page.move_slider(-150)
        map_page.move_slider(150)

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.close()
        cls.driver.quit()
