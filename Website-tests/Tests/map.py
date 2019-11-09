from selenium import webdriver
import unittest
import time
from Pages.landingPage import landingPage
from Pages.mapPage import  mapPage

class MapTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("chromedriver")

    def test_01_map_zooming(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_map()
        map = mapPage(self.driver)
        map.zoom_in_and_out()

    def test_02_map_geolocalisation(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_map()
        map = mapPage(self.driver)
        map.geolocalisation_on_off()

    def test_03_set_slider_at_70km(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_map()
        map = mapPage(self.driver)
        self.assertEqual(map.move_km_slider(), "Rayon de la recherche: 5 km")

    def test_04_new_departure_point(self):
        self.driver.get("https://www.kwili.fr/")

        landing = landingPage(self.driver)
        landing.click_map()
        map = mapPage(self.driver)
        map.research_adress("24 Rue Pasteur, 94270 Le Kremlin-Bicêtre")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()