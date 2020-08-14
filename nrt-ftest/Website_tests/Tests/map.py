import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Website_tests.Pages.MapPage import MapPage


class MapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/map"

    def test_find_itinary(self):
        """
        Test find itinary.

        Write adress and click on all tranport available.
        """
        self.driver.get(self.url)
        map_page = MapPage(self.driver)

        map_page.write_position()
        sleep(2)
        # TODO: Remove sleep function
        map_page.click_hospital()
        sleep(1)
        # TODO: Remove sleep function
        map_page.click_bus()
        sleep(2)
        # TODO: Remove sleep function
        map_page.click_car()
        sleep(2)
        # TODO: Remove sleep function
        map_page.click_walk()

    def test_zoom(self):
        """
        Test map zoom.

        Check that the user can zoom.
        """
        self.driver.get(self.url)
        map_page = MapPage(self.driver)

        map_page.write_position()
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

        Test radius slider.
        """
        self.driver.get(self.url)
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
