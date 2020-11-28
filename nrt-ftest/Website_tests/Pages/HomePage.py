class HomePage:
    """
    Classe HomePage.

    Recherche les différents élements de la page d'accueil à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_chat_card(self):
        """Clique sur la carte du chat."""
        self.driver.find_element_by_xpath("//button[@class='rcw-launcher']").click()

    def click_map_card(self):
        """Clique sur la carte de la map."""
        self.driver.find_element_by_xpath("//a[@id='map']").click()

    def click_landing_button(self):
        """Clique sur le bouton de la landing."""
        self.driver.find_element_by_xpath("//a[@class='landingLink']").click()

