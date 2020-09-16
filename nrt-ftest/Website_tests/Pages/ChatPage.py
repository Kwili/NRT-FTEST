from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class ChatPage:
    """
    Classe ChatPage.

    Recherche les différents élements de la fonctionnalité de chat à tester.
    """

    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_chat_widget(self):
        """Clique sur le chat widget."""
        self.driver.find_element_by_xpath("//button[@class='rcw-launcher']").click()
        WebDriverWait(self.driver, 2).until(
            ec.element_to_be_clickable((By.XPATH, "//h4[@class='rcw-title']")))

    def write_msg(self, msg):
        self.driver.find_element_by_xpath("//form[@class='rcw-sender']/input").send_keys(msg)
        self.driver.find_element_by_xpath("//button[@class='rcw-send']").click()
        WebDriverWait(self.driver, 2).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@class='rcw-client']/div")))
        sleep(0.5)