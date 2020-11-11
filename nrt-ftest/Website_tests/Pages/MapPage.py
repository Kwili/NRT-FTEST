from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
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

    def write_position(self, address):
        """Ecris l'adresse dans la barre de recherche et clique sur le bouton de recherche."""
        sleep(2)
        # TODO: Remove sleep function
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(address)
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//span[@class='pac-matched']"))).click()

    def is_hospital_displayed(self):
        """Clique sur le 2ème hopital dans l'arbre html."""
        try:
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[1]/div[3]/div/div[3]/div[6]')

        except NoSuchElementException:
            return False
        return True

    def _click_transport(self, i):
        """Clique sur le transport numéro i.
        :param i: int
        """
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, f"//div[@class='travelModeButtonsWrapper']/div[{i}]"))).click()

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
        slider_xpath = "//span[@class='MuiSlider-thumb MuiSlider-thumbColorPrimary jss92']"
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
