class LandingPage:
    """
    Classe LandingPage.

    Recherche les différents élements de la page /landing à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_navbar_app_link(self):
        """Clique sur le lien de l'application mobile."""
        self.driver.find_element_by_xpath("//button[text()='Application']").click()

    def click_home(self):
        """Clique sur le lien dirigeant vers la page d'accueil."""
        self.driver.find_element_by_xpath("//a[text()='KWILI']").click()

    def click_map(self):
        """Clique sur la lien dirigeant vers la map."""
        self.driver.find_element_by_xpath("//a[@href='/map']").click()

    def click_chat_widget(self):
        """Clique sur le chat widget."""
        self.driver.find_element_by_xpath("//button[@class='rcw-launcher']").click()

    def click_app_apercu_link(self):
        """Clique sur le lien de l'application mobile de la section aperçu."""
        self.driver.find_element_by_xpath("//div[@class='downloadButton']").click()
