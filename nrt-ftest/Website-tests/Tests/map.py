import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LandingPage import LandingPage
from Pages.MapPage import MapPage


class MapTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.url = "https://40.127.101.14/"

    def test_01_map_zooming(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)
        map_page.zoom_in_and_out()

    def test_02_map_geolocalisation(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)
        map_page.geolocalisation_on_off()

    def test_03_set_slider_at_70km(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)
        self.assertEqual(map_page.move_km_slider(), "Rayon de la recherche: 5 km")

    def test_04_new_departure_point(self):
        self.driver.get(self.url)

        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)
        map_page.research_adress("24 Rue Pasteur, 94270 Le Kremlin-Bicêtre")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
