from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MapPage:
    """
    Classe MapPage.

    Recherche les différents élements de la page /map à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver
        self.driver.implicitly_wait(5)

    def write_position(self):
        """Ecris l'adresse dans la barre de recherche et clique sur le bouton de recherche."""
        sleep(2)
        # TODO: Remove sleep function
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("1 rue rivoli")
        self.driver.find_element_by_xpath("//span[@class='pac-matched']").click()

    def click_hospital(self):
        """Clique sur le 2ème hopital le plus proche."""
        self.driver.find_element_by_xpath("//div[@tabindex='0']/div[3]/div/div/div[2]").click()

    def _click_transport(self, i):
        """Clique sur le transport numéro i.
        :param i: int
        """
        self.driver.find_element_by_xpath(f"//div[@class='travelModeButtonsWrapper']/div[{i}]").click()

    def click_bus(self):
        """Clique sur le transport en bus."""
        self._click_transport(1)

    def click_walk(self):
        """Clique sur le transport à pied."""
        self._click_transport(2)

    def click_car(self):
        """Clique sur le transport en voiture."""
        self._click_transport(3)

    def zoom_in(self):
        """Clique sur le zoom avant."""
        self.driver.find_element_by_xpath("//button[@title='Zoom avant']").click()

    def zoom_out(self):
        """Clique sur le zoom arrière."""
        self.driver.find_element_by_xpath("//button[@title='Zoom arrière']").click()

    def move_slider(self, offset):
        """Déplace le slider d'une valeur offset.
        :param offset: int
        """
        slider_xpath = "//span[@class='MuiSlider-thumb MuiSlider-thumbColorPrimary jss21']"
        slider = self.driver.find_element_by_xpath(slider_xpath)
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

    def no_ininary_founded_handler(self, xpath):
        """Fonction de gestion d'erreur de l'itinéraire."""
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return
        self.driver.find_element_by_xpath(xpath).click()
