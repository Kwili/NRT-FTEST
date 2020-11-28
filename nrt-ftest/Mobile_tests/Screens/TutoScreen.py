class TutoScreen:
    """
    Classe TutoScreen.

    Parcours les différents écrans tutoriels.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def button_click(self, text):
        """
        Clique sur le bouton.
        :param text: (str) Nom du bouton.
        """
        self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='{text}']").click()






