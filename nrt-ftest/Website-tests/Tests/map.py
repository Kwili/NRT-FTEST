import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LandingPage import LandingPage
from Pages.MapPage import MapPage


class MapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "http://localhost/"

    def test_01_find_itinary(self):
        self.driver.get(self.url)
        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)

        map_page.write_position()
        map_page.click_hospital()
        sleep(1)
        map_page.click_bus()
        sleep(2)
        map_page.click_car()
        sleep(2)
        map_page.click_walk()
        map_page.click_home()

    def test_02_zoom(self):
        self.driver.get(self.url)
        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)
        map_page.write_position()
        map_page.zoom_in()
        sleep(0.4)
        map_page.zoom_out()
        sleep(0.4)
        map_page.zoom_in()
        sleep(0.4)
        map_page.zoom_in()
        sleep(0.4)
        map_page.zoom_in()
        sleep(0.4)
        map_page.zoom_out()
        sleep(0.4)
        map_page.zoom_in()
        sleep(0.4)
        map_page.zoom_out()

    def test_03_radius(self):
        self.driver.get(self.url)
        landing = LandingPage(self.driver)
        landing.click_map()
        map_page = MapPage(self.driver)
        map_page.write_position()
        map_page.move_slider(150)
        map_page.move_slider(150)
        map_page.move_slider(150)
        map_page.move_slider(-150)
        map_page.move_slider(150)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
